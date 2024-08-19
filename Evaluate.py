from humanEval.evaluation import evaluateFunctionalCorrectness


def evaluate(
    sample_file: str,
    problem_file: str,
    k: str = [1,3,10],
    n_workers: int = 4,
    timeout: float = 3.0,):
    """ This function is used to acces the HumanEval frameworks evaluation function"""

    result = evaluateFunctionalCorrectness(sample_file=sample_file, problem_file=problem_file, k=k)
    return result



if __name__ == '__main__':
    problem_file = "data/output/llama3.1/n=164/passAt3.0/human-eval-v2-full.jsonl"
    sample_file = "data/output/llama3.1/n=164/passAt3.0/human-eval-v2-full_output.jsonl"
    result = evaluate(sample_file, problem_file)
    print(result)