# TODO
Do experiments
visualize experiment
example prompts
visualize example prompts
write conclusion


# Experiments
llama3.1 vs deepseeker passat10

llama3.1 basic, self-selection, self-critique

collect examples


# Possible Improvements
- The most obvious improvement is using a different model. Bigger models, and models optimized for coding would perform better. Humaneval is not the best avaialble evaluation benchmark anymore, but was a relatively small and easy one to experiment with.

- The prompts used to generate the code are not optimized or sourced from somewhere, they could certainly be optimized and would almost surelt lead to improved performanbce

- Experiment with temperature. This is an obvious hyperparameter to experiment with. Especially if you use self-reflection, or passAtk > 1. When you sample multiple samples, a lower temperature would be better than if you just generated one sample. The higher the temperature, the more variance in the supplied solutions, and the higher the chance that a succesfull sample is among them.

- Perform iterative self-reflection and critique

- Increase the amount of self-reflected samples from 3 to an higher amount

- Quite a lot of samples seem to only fail because of failed import: the LLM assumed a library was previosuly imported but wasnt (libraries like math or statistics). I dont think this is 100% fair, and would optimally change the evaluation framework to import some very common libraries on evaluation

# Iterative self-reflection/critique using tree search
Both self-relfection and self-improvement can be executed together. Performing self-improvement in X different ways, and letting the LLM decide, with which sample to continue to work. Performing this iteratveilty essentially turns this into a search problem. Managing and deciding which node to expand in this search tree effectively could potentially result in great results. This could be done with something like a Monte Carlo Search Tree. There is however the question if the LLM is good enough in judging how good code is to make this work.

# Supplying LLM more information
I would also be interested in giving the LLM additional information in order to be a better judge of how good code is. Given our very restricted current use case, where a function is essentially standalone, and its required output is clear, would it be possible to try and run code present in this search tree. Could the llm fabricate test-cases to judge how well it works, could we give error codes returned from trying to run the code back to the llm, could we run the code in a debugger and give the LLM the intermediate values when trying to run the code?

To me it seems that the combination of regarding this problem as a search-problem, and giving the LLM additional information to repair samples, could amplify the power of each other.

