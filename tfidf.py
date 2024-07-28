import math
from textblob import TextBlob

def tf(word, document):
    return (document.words.count(word) / len(document.words))

def num_documents_containing(word, documents):
    return sum(1 for document in documents if word in document.words)

def idf(word, documents):
    return math.log((1 + len(documents)) / (1 + num_documents_containing(word, documents)))

def tf_idf_score(word, document, documents_list):
    return (tf(word, document) * idf(word, documents_list))

if __name__ == "__main__":
    document1 = TextBlob(
        """Python is dynamically typed and garbage-collected. It supports multiple programming 
        paradigms, including structured (particularly procedural), object-oriented and 
        functional programming. It is often described as a "batteries included" language due 
        to its comprehensive standard library."""
    )

    document2 = TextBlob(
        """Python was invented in the late 1980s by Guido van Rossum at Centrum Wiskunde & 
        Informatica (CWI) in the Netherlands as a successor to the ABC programming language, 
        which was inspired by SETL, capable of exception handling and interfacing with the 
        Amoeba operating system. Its implementation began in December 1989. Van Rossum 
        shouldered sole responsibility for the project, as the lead developer, until 12 July 
        2018, when he announced his "permanent vacation" from his responsibilities as 
        Python's "benevolent dictator for life" (BDFL), a title the Python community bestowed 
        upon him to reflect his long-term commitment as the project's chief decision-maker 
        (he's since come out of retirement and is self-titled "BDFL-emeritus"). In January 
        2019, active Python core developers elected a five-member Steering Council to lead the 
        project."""
    )

    document3 = TextBlob(
        """Guido van Rossum began working on Python in the late 1980s as a successor to the ABC 
        programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was 
        released in 2000. Python 3.0, released in 2008, was a major revision not completely 
        backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last 
        release of Python 2."""
    )

    documents = [document1, document2, document3]

    for i, document in enumerate(documents):
        print(f'Top words in document {i + 1}')
        
        word_scores = {word: tf_idf_score(word, document, documents) for word in document.words}
        sorted_word_scores = sorted(word_scores.items(), key=lambda x: x[1], reverse=True)

        for word, score in sorted_word_scores[:2]:
            print(f'\tWord: {word}, TF-IDF={round(score, 4)}')