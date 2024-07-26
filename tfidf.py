import math

def tf(word, document_tokens):
    return (document_tokens.count(word) / len(document_tokens))

def idf(word, documents_list):
    pass

def tf_idf_score(word, document, documents_list):
    return (tf(word, document) * idf(word, documents_list))