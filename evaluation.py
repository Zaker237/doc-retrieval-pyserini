import pytrec_eval
import json


def main():
    evaluator = pytrec_eval.RelevanceEvaluator(
        qrel, {'map', 'ndcg'}
    )

if __name__ == "__main__":
    main()