# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:40:10 2019

@author: Shaheer Akram
"""

import pandas as pd
from gensim.models import word2vec as wv
import numpy as np
import nltk
from nltk.tokenize import word_tokenize

def getVectors(corpus,vectors,size):
    wordset  = set(vectors.wv.index2word)
    vec = []
    count = 0
    
    for sentence in corpus:
        feature_vec = np.zeros(vocab_size,dtype = 'object')
        for word in sentence:
            if word in wordset:
                feature_vec = np.add(feature_vec,vectors[word])
        vec.append(feature_vec.T)
        count = count+1
        print(count)
    return vec


data = pd.read_csv('final.csv')

corpus = [word_tokenize(str(sent)) for sent in data[0]]

vocab_size = 300
min_counts = 7
context = 5
n_workers = 15
down_sample = 1e-2
vectors = wv.Word2Vec(corpus,
            size = vocab_size,
            window = context,
            min_count = min_counts,
            workers = n_workers,
            sample = down_sample)

print(vectors.most_similar(''))

vec = getVectors(corpus,vectors,vocab_size)

from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

X_train,X_test,y_train,y_test = train_test_split(vec,data.rating,test_size = 0.5,random_state = 20)

clf = svm.SVC(kernel = 'rbf',cache_size = 1000,C = 0.1)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred_knn))

poly_svm = svm.SVC(kernel = 'poly')
poly_svm.fit(X_train,y_train)
y_pred_poly_svm = poly_svm.predict(X_test)

lin_svm = svm.SVC(kernel = 'linear')
lin_svm.fit(X_train,y_train)
y_pred_lin_svm = lin_svm.predict(X_test)

from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


lreg = linear_model.LogisticRegression()
lreg.fit(X_train,y_train)
y_pred_lreg = lreg.predict(X_test)

sgd = linear_model.SGDClassifier()
sgd.fit(X_train,y_train)
y_pred_sgd = sgd.predict(X_test)

mnb = MultinomialNB()
mnb.fit(X_train,y_train)
y_pred_mnb = mnb.predict(X_test)

k_range=range(1,25)
score=[]
for i in k_range:
    knn=KNeighborsClassifier(n_neighbors=11)
    knn.fit(X_train,y_train)
    y_pred_knn=knn.predict(X_test)
    score.append(accuracy_score(y_test,y_pred_knn))

rnc = RandomForestClassifier(n_estimators=100,max_depth=2,random_state=0)
rnc.fit(X_train,y_train)
y_pred_rnc = rnc.predict(X_test)

test = ["mujhe gali nahi do","tumhari amma achi ha","chutia ha kia ", "kutte ka bacha"]
n = [word_tokenize(str(sent)) for sent in test]
test = n
test = getVectors(test,vectors,vocab_size)
lreg.predict(test)



