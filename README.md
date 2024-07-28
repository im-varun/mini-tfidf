# Mini TF-IDF

This project is a basic implementation of TF-IDF measure from scratch in Python.

# About TF-IDF

TF-IDF stands for Term Frequency-Inverse Document Frequency. It is a measure of importance of a word in a document in a collection (of documents), adjusted for the fact that some words appear more frequently in general.

The tf-idf is the product of two statistics, term frequency and inverse document frequency.

  
**Term Frequency**  
It is the relative frequency of term $t$ within document $d$. It is given by:  

$tf(t, d) = \frac{f_{t, d}}{\sum_{t' \in d} f_{t', d}}$  

- $f_{t, d} =$ number of times term $t$ occurs in document $d$  
- $\sum_{t' \in d} f_{t', d} =$ total number of terms in document $d$  

  
**Inverse Document Frequency**  
It is a measure of how much information the word provides, i.e., how common or rare it is across all documents. It is the logarithmically scaled inverse fraction of the documents that contain the word (obtained by dividing the total number of documents by the number of documents containing the term, and then taking the logarithm of that quotient).  

$idf(t, D) = log \frac{N}{|\{d:\text{ }d \in D{\text{ and }}t \in d\}|}$  

- $N =$ total number of documents in the collection $N = |D|$  
- $|\{d:\text{ }d \in D{\text{ and }}t \in d\}| =$ number of documents where the term $t$ appears. If the term is not in the collection, this will lead to a division-by-zero. It is therefore common to adjust the numerator $1 + N$ and denominator to $1 + |\{d:\text{ }d \in D{\text{ and }}t \in d\}|$.  

  
**Term Frequency-Inverse Document Frequency**  
$tfidf(t, d, D) = tf(t, d) \cdot idf(t, D)$

# References

Wikipedia contributors. (2024, July 26). Tf–idf. In Wikipedia, The Free Encyclopedia. Retrieved 18:13, July 28, 2024, from https://en.wikipedia.org/w/index.php?title=Tf%E2%80%93idf&oldid=1236851603

# Disclaimer

This project is for educational purposes only. The from-scratch implementation of TF-IDF measure may not be completely accurate or optimized. It is intended as a learning exercise to understand the underlying concepts of famous methodologies and algorithms.