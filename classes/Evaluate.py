from humanEval.evaluation import evaluateFunctionalCorrectness


def evaluate(
    sample_file: str,
    problem_file: str,
    k: str = "1,10,100",
    n_workers: int = 4,
    timeout: float = 3.0,):
    result = evaluateFunctionalCorrectness(sample_file=sample_file, problem_file=problem_file)
    return result



if __name__ == '__main__':
    sample_file = "data/output/human-eval-v2-20210705_output_0.jsonl"
    problem_file = "data/human-eval-v2-20210705.jsonl"
    result = evaluate(sample_file, problem_file)
    print(result)