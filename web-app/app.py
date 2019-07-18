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

def readword2vec():    
    f = open('../wv.pickle','rb')
    vectors = p.load(f)
    vocab_size = vectors.wv.vectors.shape[1]
    return vectors,vocab_size


app = Flask(__name__)

#to render the home template aka index.html
@app.route('/',methods = ['GET','POST'])
def home():
    return render_template('index.html')


#post api to get data from user and send result to user
@app.route('/check', methods = ['GET','POST'])
def check():
    from keras.models import load_model
    import gensim.models.word2vec as wv
    if request.method == 'POST':
        sentence = ['']
        sentence = [request.form.get('sent')]
        model = load_model('../deep.h5')
        vectors,vocab_size = readword2vec()
        sentence = [sent.split() for sent in sentence] 
        X_sent = getVectors(sentence,vectors,vocab_size)
        X_sent = np.array(X_sent)
        pred = model.predict(X_sent)
        pred = np.argmax(pred,axis = 1)
        
        return render_template('result.html',result = pred)
        


if __name__ == '__main__':
    app.run(debug= True, port= 5000)





