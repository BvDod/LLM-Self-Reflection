from classes.Parser import ProblemParser
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

class Coder():
    """Class which defines the LLM and Coding Bot"""

    def __init__(self, model_name="llama3.1", usePrompt=False):
        
        self.settings = {
            model_name : "llama3.1",
        }
        
        
        self.llm = Ollama(model=model_name)
        self.usePrompt = usePrompt

        self.prompt = ChatPromptTemplate.from_messages([
        ("system", "You are trying to create Python 3 functions that both run and perform the correct action. You are given the name of a function. You are required to return the code that should be a function with that name. Only return the code"),
        ("user", "{input}")])

        if usePrompt:
            self.chain = self.prompt | self.llm 
        else:
            self.chain = self.llm
    
    def invokePrompt(self, prompt: str, stripDef=False) -> str:
        """ Given a prompt, invokes our Coder and returns response"""
        
        if self.usePrompt:
            response = self.chain.invoke({"input": prompt})
        else:
            response = self.chain.invoke(prompt)

        if stripDef:
            response = stripDefFunction(response)
        return response



def stripDefFunction(code: str) -> str:
    
    # Borrow from: https://github.com/FSoft-AI4Code/CodeCapybara
    # "pad to four space to avoid `unindent` error"
    def pad_spaces(s, num=4):
        n = 0
        while n < len(s) and s[n] == " ":
            n += 1
        if n != num:
            s = " " * num + s[n:]
        return s

    """If a function starts like "def function1:", strips that """
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
