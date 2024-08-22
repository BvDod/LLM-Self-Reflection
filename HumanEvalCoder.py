from classes.Parser import ProblemParser
from classes.Coder import Coder
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from classes.Evaluate import evaluate
import time




if __name__ == "__main__":
    
    
    problem_file = "data/human-eval-v2-full.jsonl"
    printSamples = True  # Print every single prompt and generated sample
    # model_name = "deepseek-coder-v2" # "llama3.1" or "deepseek-coder-v2"
    model_name = "llama3.1"
    passAtK = 10

    start_time = time.time()
    codeBot = Coder(printSamples=printSamples, model_name=model_name)
    parser = ProblemParser(problem_file, codeBot.settings)

    # Only get prompts for each problem
    problems = parser.getProblems()  # list of (task_id, prompt)

    # Generate LLM responses
    llm_responses = []
    for i, (task_id, prompt) in enumerate(problems):
        
        # Generate sampe amount according to passatK setting
        for j in range(passAtK):
            response = codeBot.getSample(prompt, stripDef=True)
            llm_responses.append((task_id, response))
        
        if i%10 == 0:
            print(f"Prompt progress: {i}/{len(problems)}")
    print(f"Finished {len(llm_responses)} prompts")
    

    # Calculate runtime
    length_seconds = time.time() - start_time
    if length_seconds < 60:
        runtime = f"{int(length_seconds)}s"
    elif length_seconds < 3600:
        min = length_seconds//60
        sec = length_seconds%60
        runtime = f"{int(min)}m {int(sec)}s"
    else:
        hour = length_seconds//3600
        min = length_seconds%3600
        runtime = f"{int(hour)}h {int(min)}m"
    
    # Save responses to expected JSONL file
    parser.saveResponses(llm_responses)

    # Evaluated files we just saved
    results = evaluate(parser.settings["filename_out"], parser.settings["filename_in"])
    print(results)
    print(runtime)
    
    # Save test settings and results for easilt accesible (redudnant) access
    with open('results.txt','a') as file:
        file.write(f'{codeBot.settings}, {parser.settings}: {results} , runtime: {runtime}\n')
    