#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:24:37 2019

@author: shaheer
"""


from flask import Flask,render_template,request,redirect,jsonify
import numpy as np
import pandas as pd
import pickle as p
from keras.models import load_model
import gensim.models.word2vec as wv
from keras import backend as k


def getVectors(corpus,vectors,size):
    wordset = set(vectors.wv.index2word) #Checks if the word is in the Word2vec corpus 
    vec = []
    counter = 0
    for words in corpus:    
        featureVec = np.zeros(size,dtype="object")
        for word in words:
            if word in wordset:
                featureVec = np.add(featureVec,vectors[word])
        vec.append(featureVec.T)
        counter = counter + 1
        #print(counter)
    return vec

def readModel():    
    f = open('wv.pickle','rb')
    vectors = p.load(f)
    f.close()
    vocab_size = vectors.wv.vectors.shape[1]
    model = load_model('deep.h5')
    return  model,vectors,vocab_size


app = Flask(__name__)

'''
if request method is post api will make pridiction and show result on index.html
if request method is get api will simply render index.html
'''
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        sentence = ['']
        sentence = [request.form.get('sent')]
        model,vectors,vocab_size = readModel()
        sentence = [sent.split() for sent in sentence] 
        X_sent = getVectors(sentence,vectors,vocab_size)
        X_sent = np.array(X_sent)
        pred = model.predict(X_sent)
        k.clear_session()
        pred = np.argmax(pred,axis = 1)
        del model
        del vectors
        del sentence
        del vocab_size
        del X_sent
        return render_template('index.html',result = pred)
    else:
        return render_template('index.html')

        


if __name__ == '__main__':
    app.run(debug= True, port= 5000)





