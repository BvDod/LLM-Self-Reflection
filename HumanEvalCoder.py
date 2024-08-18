from classes.Parser import ProblemParser
from classes.Coder import Coder
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate



if __name__ == "__main__":
    

    codeBot = Coder(usePrompt=True)
    # parser = ProblemParser("./data/example_problem.jsonl")
    parser = ProblemParser("./data/human-eval-v2-20210705.jsonl")

    # Only get prompts for each problem
    prompts = parser.getPrompts()

    # Generate LLM responses
    llm_responses = []
    for i, prompt in enumerate(prompts):
        response = codeBot.invokePrompt(prompt, stripDef=True)
        llm_responses.append(response)
        print(f"Prompt {i}/{len(prompts)}")
        print(f"Prompt:\n {prompt.strip("\n")}\nResult:\n {response}\n")
    
    # Save responses to expected JSONL file
    parser.saveResponses(llm_responses)
    