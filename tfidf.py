import math

def get_document_tokens(document):
    pass

def tf(word, document):
    document_tokens = get_document_tokens(document)
    return (document_tokens.count(word) / len(document_tokens))

def num_documents_containing(word, documents):
    count = 0

    for document in documents:
        document_tokens = get_document_tokens(document)

        if word in document_tokens:
            count += 1

    return count

def idf(word, documents):
    return math.log(len(documents) / (1 + num_documents_containing(word, documents)))

def tf_idf_score(word, document, documents_list):
    return (tf(word, document) * idf(word, documents_list))