import numpy as np
from collections import Counter


class CountVectorizer:
    """
    Class for document-term matrix preparation:
    1. Tokenization (+ lowercase transform if required)
    2. Counting of each token in a document
    3. Building a vector of frequencies of tokens from vocabulary

    Args for init:
    - lowercase: transform all tokens to lowercase format or not (default=True)

    """

    def __init__(self, lowercase: bool = True):
        self.lowercase = lowercase
        self._feature_names = {}

    def fit_transform(self, corpus: list) -> np.array:
        """
        Args:
        - corpus: list of sentences

        Return:
        - document-term matrix

        """
        corpus_tokenized = [
            doc.lower().split(' ') if self.lowercase else doc.split(' ') for doc in corpus
        ]
        corpus_counts = [
            Counter(doc_tokenized) for doc_tokenized in corpus_tokenized
        ]

        # get set of all tokens, delete '' token if exists (connected with '' sentence) and sort it
        self._feature_names = sorted(
            set.union(*[set(doc_counts.keys()) for doc_counts in corpus_counts]) - set([''])
        )

        # raise error if vocabulary is empty
        # (inspired by sklearn CountVectorizer)
        if len(self._feature_names) == 0:
            raise ValueError('Empty vocabulary')

        # map each token in doc to its count value for each doc on corpus
        return np.array(
            [[doc_counts[token] for token in self._feature_names] for doc_counts in corpus_counts]
        )

    def get_feature_names(self):
        return self._feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
