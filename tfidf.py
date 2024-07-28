import math
from textblob import TextBlob

def tf(word, document):
    return (document.words.count(word) / len(document.words))

def num_documents_containing(word, documents):
    return sum(1 for document in documents if word in document.words)

def idf(word, documents):
    return math.log(len(documents) / (1 + num_documents_containing(word, documents)))

def tf_idf_score(word, document, documents_list):
    return (tf(word, document) * idf(word, documents_list))