from classes.Parser import ProblemParser
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
import random

class Coder():
    """Class which defines the LLM and Coding Bot"""

    def __init__(self, model_name="llama3.1", printSamples=False):
        
        self.settings = {
            "model_name" : model_name,
        }
        
        self.llm = Ollama(model=model_name)
        self.printSamples = printSamples
        self.self_selection = False

        self.prompt = ChatPromptTemplate.from_messages([
        ("system", """You are trying to create Python 3 functions that both run and perform the correct action. 
         You are given the name of a function. You are required to return the code that should be a function with
         that name. Only return the code"""),
        ("user", "{input}")])

        # Prompt used for self-selection
        self.selection_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are given 3 different Python 3 functions, that are supposed to both run and perform the correct action.
        Critisize each of the three implementations on why they wouldnt work or perform the correct action, and then select the 
        implementation that is the best. Depending on the best function, ALWAYS end the message in precisely the following format:
        'Selected function: function x', where x is 1, 2 or 3"""),
        ("user", "Function 1: {function1}\n Function 2: {function2}\n Function 3: {function3}")])

        self.chain = self.prompt | self.llm 

        if self.self_selection:
            self.selection_chain = self.selection_prompt | self.llm

    
    def invokePrompt(self, prompt: str) -> str:
        """ Given a prompt, invokes our Coder and returns response"""
        
        response = self.chain.invoke({"input": prompt})
        return response



    def getsSelfSelectionSample(self, prompt):
        """Generates 3 random samples and lets the LLM select which is best, return said best sample"""
        
        # Generate 3 candidates
        response_candidates = []
        for i in range(3):
            response = self.invokePrompt(prompt)
            if self.printSamples:
                response_cleaned = cleanCodeFormatting(response)
                if self.printSamples:
                    print(f"Function {i}:\n {response_cleaned.strip("\n")}\n")
            response_candidates.append(response)
        
        # Asks to critique samples and select best
        selection_response = self.selection_chain.invoke({"function1": response_candidates[0], 
                                                          "function2": response_candidates[1], 
                                                          "function3": response_candidates[2]})
        if self.printSamples:
            print(selection_response)

        # Gets best function int from response prompt
        for i, c in enumerate(selection_response[::-1]):
            if c.isdigit():
                best_function = int(c)
                break
        print(best_function)
        if not best_function in [1,2,3]:
            print("selected random")
            best_function = random.choice([1,2,3])
       
        return response_candidates[best_function-1]

    def getsSelfReflectionSample(self, prompt):   
        """Generates code sample, critique using LLM, then rewrite using LLM"""

        response = self.invokePrompt(prompt)
        critique = self.CRITISIZE(RESPONSE)
        rewritten = self.REWRITE(reponse, critique)

    
    def getSample(self, prompt: str, stripDef=False) -> str:
        """Get a cleaned output sample given a prompt using current LLM settings (incl reflection)"""

        if self.self_selection:
            response = self.getsSelfSelectionSample(prompt)
        else:
            response = self.invokePrompt(prompt)

        if stripDef:
            response = cleanCodeFormatting(response)
        
        if self.printSamples:
            print(f"Prompt:\n {prompt.strip("\n")}\nResult:\n {response}\n")

        return response



def cleanCodeFormatting(code: str) -> str:
    """Strips everything before def function: AND changes TABS to spaces """
    
    # Borrow from: https://github.com/FSoft-AI4Code/CodeCapybara
    # "pad to four space to avoid `unindent` error"
    def pad_spaces(s, num=4):
        n = 0
        while n < len(s) and s[n] == " ":
            n += 1
        if n != num:
            s = " " * num + s[n:]
        return s

    line_start_def = code.find("\ndef ")
    index = code[line_start_def+2:].find("\n")
    code = code[line_start_def+index+4:]

    if code[-4:] == "\n```":
        code = code[:-4]
    
    code = pad_spaces(code, 4)
    return code



if __name__ == "__main__":
    
    codeBot = Coder()
    response = codeBot.invokePrompt("def return1():\n")
    print(response)
