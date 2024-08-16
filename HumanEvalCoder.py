from classes.Parser import ProblemParser
from classes.Coder import Coder
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate



if __name__ == "__main__":
    

    codeBot = Coder(usePrompt=True)
    # parser = ProblemParser("./data/example_problem.jsonl")
    parser = ProblemParser("./data/human-eval-v2-20210705.jsonl")

    # Only get prompts for each problem
    prompts = parser.getPrompts(randomAmount=10)

    # Generate LLM responses
    llm_responses = []
    for i, prompt in enumerate(prompts):
        response = codeBot.invokePrompt(prompt, stripDef=True)
        llm_responses.append(response)
        print(f"Prompt {i}/{len(prompts)}")
        print(f"Prompt: {prompt.strip("\n")}\nResult: {response}\n")
    
    # Save responses to expexted JSONL file
    parser.saveResponses(llm_responses)
    