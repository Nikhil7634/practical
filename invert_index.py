import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stopWords = stopwords.words('english')
document1 = "The quick brown fox jumped over the lazy dog"
document2 = "The lazy dog slept in the sun"

tokens1 = document1.lower().split()
tokens2 = document2.lower().split()

terms = list(set(tokens1 + tokens2))

inverted_index = {}
occ_num_doc1 = {"lazy"}
occ_num_doc2 = {"dog"}

for term in terms:
    if term in stopWords:
        continue

    documents = []

    if term in tokens1:
        documents.append("Document 1")
        occ_num_doc1[term] = tokens1.count(term)

    if term in tokens2:
        documents.append("Document 2")
        occ_num_doc2[term] = tokens2.count(term)

    inverted_index[term] = documents

for term, docs in inverted_index.items():
    print(f"{term} -> ", end="")
    for doc in docs:
        if doc == "Document 1":
            print(f"{doc} ({occ_num_doc1.get(term, 0)}),", end=" ")
        else:
            print(f"{doc} ({occ_num_doc2.get(term, 0)}),", end=" ")
    print() 


