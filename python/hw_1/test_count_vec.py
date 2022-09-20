import numpy as np

from utils import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer as CVec


def test_ordinary_case():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    
    true_vocab = ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
                  'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    true_matrix = np.array([[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]])
    
    assert sorted(vectorizer.get_feature_names()) == sorted(true_vocab)
    
    assert (true_matrix[:, np.argsort(true_vocab)] == count_matrix[:, np.argsort(vectorizer.get_feature_names())]).all()


def test_ordinary_case_with_sklearn():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    
    vec = CVec()
    true_matrix = vec.fit_transform(corpus).toarray()
    true_vocab = list(vec.vocabulary_.keys())
    
    assert sorted(vec.get_feature_names()) == sorted(true_vocab)
    
    assert (true_matrix == count_matrix).all()
    

def test_edge_case_1():
    corpus = [
        '',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    
    vec = CVec()
    true_matrix = vec.fit_transform(corpus).toarray()
    true_vocab = list(vec.vocabulary_.keys())
    
    assert sorted(vec.get_feature_names()) == sorted(true_vocab)
    
    assert (true_matrix == count_matrix).all()
    

def test_edge_case_2():
    corpus = [
        'Pasta Pasta Pasta Pasta Pasta Pasta Pasta',
        ''
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    
    vec = CVec()
    true_matrix = vec.fit_transform(corpus).toarray()
    true_vocab = list(vec.vocabulary_.keys())
    
    assert sorted(vec.get_feature_names()) == sorted(true_vocab)
    
    assert (true_matrix == count_matrix).all()
    

def test_edge_case_3():
    corpus = [
        'Pasta'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    
    vec = CVec()
    true_matrix = vec.fit_transform(corpus).toarray()
    true_vocab = list(vec.vocabulary_.keys())
    
    assert sorted(vec.get_feature_names()) == sorted(true_vocab)
    
    assert (true_matrix == count_matrix).all()
    