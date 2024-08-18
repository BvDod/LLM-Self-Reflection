from classes.Parser import ProblemParser
from classes.Coder import Coder
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from classes.Evaluate import evaluate


if __name__ == "__main__":
    

    codeBot = Coder(usePrompt=True)
    # parser = ProblemParser("./data/example_problem.jsonl")
    parser = ProblemParser("./data/example_problem.jsonl", codeBot.settings)

    # Only get prompts for each problem
    prompts = parser.getPrompts()

    # Generate LLM responses
    llm_responses = []
    for i, prompt in enumerate(prompts):
        response = codeBot.invokePrompt(prompt, stripDef=True)
        llm_responses.append(response)
        
        if i%10 == 0:
            print(f"Prompt {i}/{len(prompts)}")
    print(f"Finished {len(llm_responses)} prompts")
    
    # Save responses to expected JSONL file
    parser.saveResponses(llm_responses)

    results = evaluate(parser.settings["filename_out"], parser.settings["filename_in"])
    
    # Save test settings and results for easy (redudnant) access
    with open('results.txt','a') as file:
        file.write(f'{codeBot.settings}, {parser.settings}: {results} \n')
    