import os

from pyserini.dsearch import SimpleDenseSearcher, TctColBertQueryEncoder
from utils import load_tsv_file

TEXT_DATA_FILE = "./2019qrels-docs.txt"

def main():
    test_data = load_tsv_file(TEXT_DATA_FILE)
    

    encoder = TctColBertQueryEncoder('castorini/tct_colbert-msmarco')
    searcher = SimpleDenseSearcher.from_prebuilt_index(
        'msmarco-passage-tct_colbert-hnsw',
        encoder
    )
    for data in test_data[:2]:
        hits = searcher.search(data[1])

        for i in range(0, 10):
            print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.5f}')

if __name__ == "__main__":
    main()