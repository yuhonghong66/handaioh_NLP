from gensim.models import KeyedVectors
from mysite.settings import BASE_DIR
from pathlib import Path

data_path = str(Path(BASE_DIR).joinpath('handaioh_NLP/utils/data/word2vec.300d.ja.txt').resolve())
model = KeyedVectors.load_word2vec_format(data_path)


def Candidate_selector(word, topn=3):
    return [word for (word, _) in model.most_similar(word, topn=topn)] if word in model.wv.vocab else None

if __name__ == '__main__':
    Candidate_selector('NASA')
