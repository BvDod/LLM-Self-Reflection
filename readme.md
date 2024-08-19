# TODO
implement self-critiqie and improvement


Do experiments
visualize experiment
example prompts


# TODO
Both self-relfection and self-improvement can be executed together. Performing self-improvement in X different ways, and letting the LLM decide, with which sample to continue to work. Performing this iteratveilty essentially turns this into a search problem. Managing and deciding which node to expand in this search tree effectively could potentially result in great results. This could be done with something like a Monte Carlo Search Tree. There is however the question if the LLM is good enough in judging how good code is to make this work.

I would also be ineterested in giving the LLM additional information in order to be a better judge of how good code is. Given our very restricted current use case, where a function is essentially standalone, and its required output is clear, would it be possible to try and run code present in this search tree. Could the llm fabricate test-cases to judge how well it works, could we give error codes returned from trying to run the code back to the llm, could we run the code in a debugger and give the LLM the intermediate values when trying to run the code?

To me it seems that the combination of regarding this problem as a search-problem, and giving the LLM additional information to repair samples, could amplify the power of each other.

