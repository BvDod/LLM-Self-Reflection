# LLM Python-code generation: self-improvement 
This project demonstrates and implements **self-selection** and **self-critique** when generating Python code using an LLM, and includes code to easily evaluate performance on the HumanEval evaluation dataset. This project is built using LangGraph and Ollama. Multiple evaluation experiments have been done and are presented on this GitHub page.


## Self-Selection
![llm](https://github.com/user-attachments/assets/cbc6ec86-1e32-4483-a322-2a5045a50aad)

Self-selection is implemented by making the LLM output 3 different outputs for the requested prompt. The 3 outputs are then fed back into the LLM, and the LLM is asked to critisize and select the best of the three generated functions. This selected function is then taken as the final output.

## Self-Critique
![llm2](https://github.com/user-attachments/assets/7e8bcab1-c207-47ea-af4d-6e2974fd59cf)

Self-critique is implemented by first making the LLM output a single sample for the requested prompt. In a second prompt, this generated function is fed back into the LLM, and the LLM is asked to critisize the code. In a third and final prompt, the LLM is asked to fix the generated code using the given feedback. This is then used as the final output


## Evaluation experiments
### LLM model & Pass@K
First, I compared the popular model llama 3.1 (8b) to a model that has been finetuned on coding tasks: deepseek-coder-v2 (8B).
![output1](https://github.com/user-attachments/assets/67722b31-9f5b-4189-8d2c-c332995b93df)

As you can see, there is a rather big difference between pass@1, pass@3, and pass@10. This is a good result for the potential effectivity of self-selection; if multiple samples are generated, there is a lot bigger chance that a correct sample is among them, than if just 1 sample is generated. Interestingly, the difference in performance seems to decrease as the amount of samples increases, and at pass@10, the difference is almost the same.
![output2](https://github.com/user-attachments/assets/55884eec-f1f5-460c-bee5-1ee48f694720)

### Self-selection
A slightly higher,but apparent, higher pass@1 was found for when self-selection was used versus when it was not. However, its still a lot lower than the pass@3 without self-reflection. This means that even though the LLM can somewhat select the best option, its still very far from optimally selecting the best option. Even though its clearly not an optimal usage of computational budget, it shows how self-selection can increase performance.

### Self-critique
Self-critique leads to a much lower score than even the default. This suggests that the step where the code is improved, tends to introduce more errors than it fixes. This does not mean self-critique is useless, just that with THIS llm model, more issues get created than fixed.

## HumanEval




## Possible/future Improvements
### Low hanging fruit/optimizations
- Use different model. Bigger models, and models optimized for coding would perform better. 
- Humaneval is not the best avaialble evaluation benchmark anymore, but was a relatively small and easy one to experiment with.
- The prompts used to generate the code are not optimized or sourced from somewhere, they could certainly be optimized and would almost surelt lead to improved performanbce
- Experiment with temperature. This is an obvious hyperparameter to experiment with. Especially if you use self-reflection, or passAtk > 1. When you sample multiple samples, a lower temperature would be better than if you just generated one sample. The higher the temperature, the more variance in the supplied solutions, and the higher the chance that a succesfull sample is among them.
- Increase the amount of self-reflected samples from 3 to an higher amount
- Quite a lot of samples seem to only fail because of failed import: the LLM assumed a library was previosuly imported but wasnt (libraries like math or statistics). I dont think this is 100% fair, and would optimally change the evaluation framework to import some very common libraries on evaluation

### Iterative self-reflection/critique and/or using tree search
Both self-relfection and self-improvement can be executed together, and in an iterative fashion. Performing self-improvement in X different ways, and letting the LLM decide, with which sample to continue to work. Performing this iteratveilty essentially turns this into a search problem. Managing and deciding which node to expand in this search tree effectively could potentially result in great results. This could be done with something like a Monte Carlo Search Tree. There is however the question if the LLM is good enough in judging how good code is to make this work.

### Supplying LLM more information
I would also be interested in giving the LLM additional information in order to be a better judge of how good code is. Given our very restricted current use case, where a function is essentially standalone, and its required output is clear, would it be possible to try and run code present in this search tree. Could the llm fabricate test-cases to judge how well it works, could we give error codes returned from trying to run the code back to the llm, could we run the code in a debugger and give the LLM the intermediate values when trying to run the code?

To me it seems that the combination of regarding this problem as a search-problem, and giving the LLM additional information to repair samples, could amplify the power of each other.

## Self-Reflection: output example
### Generated functions
Function 1:
```
has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers.sort()  # Sort the list of numbers in ascending order
    for i in range(len(numbers) - 1):  # Iterate over the sorted list
        # Check if adjacent elements are within threshold distance
        if abs(numbers[i] - numbers[i + 1]) < threshold:  
            return True
    return False
```


Function 2:
```
has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
    return False
```

Function 3:
```
has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers.sort()  # Sort the list in ascending order
    for i in range(len(numbers) - 1):  # Iterate over the sorted list
        if abs(numbers[i] - numbers[i + 1]) <= threshold: 
            # If the difference is less than or equal to the threshold, return True 
            return True
    # If no pair of elements is within the threshold, return False
    return False  
```
### LLM self-selection response
```
Here's a critique of each implementation:

**Function 1**
The issue with this function is that it only checks for pairs of adjacent numbers in the sorted list. It does not consider non-adjacent numbers that may be closer than the threshold. For example, if the input list is `[1.0, 2.8, 3.0]`, the function will return `False` because it only checks for the pair `(2.0, 3.0)` and not the pair `(1.0, 2.8)`.

**Function 2**
This function correctly checks all pairs of numbers in the input list to see if any two numbers are closer than the threshold. However, it has a time complexity of O(n^2), which may be inefficient for large lists of numbers.

**Function 3**
The issue with this function is that it also only checks for adjacent numbers in the sorted list. Just like Function 1, it does not consider non-adjacent numbers that may be closer than the threshold.

After critiquing each implementation, I would say that **Function 2** is the best implementation because it correctly checks all pairs of numbers to see if any two numbers are closer than the threshold. While its time complexity is O(n^2), which may not be efficient for large lists, it is still a correct and working solution.

Therefore, the final answer is:
Selected function: 2
```


