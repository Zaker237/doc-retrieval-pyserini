import os

from pyserini.dsearch import SimpleDenseSearcher, TctColBertQueryEncoder
from utils import load_tsv_file, save_file

TEXT_DATA_FILE = "./msmarco-test2019-queries.tsv"
RESULT_FILE = "./msmarco-test2019-results.tsv"

def main():
    test_data = load_tsv_file(TEXT_DATA_FILE)
    

    encoder = TctColBertQueryEncoder('castorini/tct_colbert-msmarco')
    searcher = SimpleDenseSearcher.from_prebuilt_index(
        'msmarco-passage-tct_colbert-hnsw',
        encoder
    )
    result_data = []
    for data in test_data[:2]:
        hits = searcher.search(data[1])

        for i in range(0, 100):
            result_string = f"{data[0]} Q0 {hits[0].docid:7} {i+1} {hits[0].score:.5f} IndriQueryLikelihood"
            result_data.append(result_string)
            print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.5f}')

    save_file(data, RESULT_FILE)

    print("______End________")
        

if __name__ == "__main__":
    main()