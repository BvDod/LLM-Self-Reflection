# LLM python generation: self-selection & self-critique
This project demonstrates and implements self-selection and self-critique when generating Code using an LLM, and includes code to evaluate performance on the HumanEval evaluation dataset. This project is built using LangGraph and Ollama. Multiple evaluation experiments have been done and are presented on this GitHub page.


## Self-Selection
![llm](https://github.com/user-attachments/assets/cbc6ec86-1e32-4483-a322-2a5045a50aad)

## Self-Critique
![llm2](https://github.com/user-attachments/assets/7e8bcab1-c207-47ea-af4d-6e2974fd59cf)

## Output Samples

## Evaluation experiments

## Codebase

## HumanEval

## Future improvements
# TODO
Both self-reflection and self-improvement can be executed together. Performing self-improvement in X different ways, and letting the LLM decide, with which sample to continue to work. Performing this iteratveilty essentially turns this into a search problem. Managing and deciding which node to expand in this search tree effectively could potentially result in great results. This could be done with something like a Monte Carlo Search Tree. There is however the question if the LLM is good enough in judging how good code is to make this work.

I would also be interested in giving the LLM additional information in order to be a better judge of how good code is. Given our very restricted current use case, where a function is essentially standalone, and its required output is clear, would it be possible to try and run code present in this search tree. Could the llm fabricate test-cases to judge how well it works, could we give error codes returned from trying to run the code back to the llm, could we run the code in a debugger and give the LLM the intermediate values when trying to run the code?

To me it seems that the combination of regarding this problem as a search-problem, and giving the LLM additional information to repair samples, could amplify the power of each other.

