from classes.Parser import ProblemParser
from classes.Coder import Coder
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from classes.Evaluate import evaluate


if __name__ == "__main__":
    
    printSamples = False    # Print every single prompt and generated sample

    codeBot = Coder(usePrompt=True, printSamples=printSamples)
    parser = ProblemParser("data/example_problem.jsonl", codeBot.settings)
    passAtK = 10

    # Only get prompts for each problem
    problems = parser.getProblems()  # list of (task_id, prompt)

    # Generate LLM responses
    llm_responses = []
    for i, (task_id, prompt) in enumerate(problems):
        
        # Generate sampe amount according to passatK setting
        for i in range(passAtK):
            response = codeBot.invokePrompt(prompt, stripDef=True)
            llm_responses.append((task_id, response))
        
        if i%10 == 0:
            print(f"Prompt progress: {i}/{len(problems)}")
    print(f"Finished {len(llm_responses)} prompts")
    
    # Save responses to expected JSONL file
    parser.saveResponses(llm_responses)

    # Evaluated files we just saved
    results = evaluate(parser.settings["filename_out"], parser.settings["filename_in"])
    print(results)
    
    # Save test settings and results for easilt accesible (redudnant) access
    with open('results.txt','a') as file:
        file.write(f'{codeBot.settings}, {parser.settings}: {results} \n')
    