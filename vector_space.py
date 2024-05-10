from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import nltk
from nltk.corpus import stopwords
import numpy as np
from numpy.linalg import norm

train_set = ["The sky is blue.", "The sun is bright."]
test_set = ["The sun in the sky is bright."]

nltk.download('stopwords')
stopWords = stopwords.words('english')

vectorizer = CountVectorizer(stop_words=stopWords)
transformer = TfidfTransformer()

trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()

testVectorizerArray = vectorizer.transform(test_set).toarray()

print("Training set TF-IDF array:", trainVectorizerArray)
print("Test set TF-IDF array:", testVectorizerArray)

cosine_similarity = lambda a, b: round(np.inner(a, b) / (norm(a) * norm(b)), 3)

for vector in trainVectorizerArray:
    print("Training set vector:", vector)
    for testV in testVectorizerArray:
        print("Test set vector:", testV)
        cosine = cosine_similarity(vector, testV)
        print("Cosine similarity:", cosine)

transformer.fit(trainVectorizerArray)
print("Transformed training set (TF-IDF):")
print(transformer.transform(trainVectorizerArray).toarray())

transformer.fit(testVectorizerArray)
print("Transformed test set (TF-IDF):")
tfidf_test_set = transformer.transform(testVectorizerArray)
print(tfidf_test_set.todense())
