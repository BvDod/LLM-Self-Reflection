import json
import os.path



class ProblemParser():
    """ Class which handles the parsing of the HumanEval JSONL, and
    the dumping of answers to a JSONL """

    def __init__(self, file: str):
        self.file_name = file
        self.problems = self.readJsonLines(file) # List of dict of each problem


    def readJsonLines(self, file: str) -> list[dict]:
        """ Reads JSONL with all problems and return as list of dict"""

        if not os.path.isfile(file):
            raise Exception(f"File doesnt exit: {file}")

        if not file[-6:] == ".jsonl" and not file[-6:] == ".JSONL":
         
           raise Exception(f"File isnt JSONL file: {file}") 
        
        with open(file) as f:
            data = [json.loads(line) for line in f]
        return data
    

    def getPrompts(self) -> list[str]:
        """ Return List of all prompts in the parsed JSONl """
        
        return [problem["prompt"] for problem in self.problems]


    def saveResponses(self, responses: list[str]) -> None:
        """ Save responses to output File """
        
        if not len(responses) == len(self.problems):
            raise Exception(f"length of parsed problems differs from length of responses ({len(self.problems)} vs {len(responses)})")


        output = [] # contains dicts for every JSON line
        for i, problem in enumerate(self.problems):
            JsonLine = {}
            JsonLine["task_id"] = problem["task_id"]
            JsonLine["completion"] = responses[i]
            output.append(JsonLine)    
        
        # Write to unique JSONL file
        filename = self.getOutputName()
        with open(filename, 'w') as outfile:
            for entry in output:
                json.dump(entry, outfile)
                outfile.write('\n')


    def getOutputName(self) -> str:
        "Get name to output to, make sure it doesnt exist yet"
        i = 0
        output_name = self.file_name[:-6] + f"_output_{i}" + ".jsonl"
        while os.path.isfile(output_name):
            i += 1
            output_name = self.file_name[:-6] + f"output_{i}" + ".jsonl"
        return output_name


        
        



if __name__ == "__main__":
    
    # Load example file
    parser = ProblemParser("./data/example_problem.jsonl")
    
    # Only get prompts for each problem
    prompts = parser.getPrompts()

    # Generate LLM responses
    llm_responses = []
    for prompt in prompts:
        response = "placeholder" # LLM generating response would happen here
        llm_responses.append(response)
    
    # Save responses to expexted JSONL file
    parser.saveResponses(llm_responses)

