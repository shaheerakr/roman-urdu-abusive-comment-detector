# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:25:17 2018

@author: Shaheer Akram
"""

import pandas as pd
import csv
import re

df1 = pd.read_csv("comments-0EKIdWNQ2rc.csv", encoding = 'utf-8')
df2 = pd.read_csv("comments-HG3WBLRFWZc.csv", encoding = 'utf-8')
frames = [df1,df2]
merge = pd.concat(frames)
del merge['hasReplies']
del merge['numberOfReplies']
merge['commentText'] = merge['commentText'].map(str) + merge['replies.commentText'].map(str)
del merge['replies.commentText']
merge.head()
merge.to_csv("all.csv")
data = pd.read_csv('all.csv',index_col = 0)
corpus = []
#X = data['commentText']
for i in range(len(X)):
    #review = re.sub('nan',' ',str(X[i]))
    #review = re.sub('http\S+',' ',str(X[i]))
    review = re.sub('[^a-zA-Z]',' ',str(X[i]))
    review = review.lower()         #run this for last ittration only
    review = review.split()
    review = ' '.join(review)
    corpus.append(review)
clean = pd.DataFrame(corpus)
clean.columns = ['comment']
clean['comment'].str.contains("https").astype(int).sum()
X = clean['comment']
clean.to_csv("clean.csv")
data = pd.read_csv('clean.csv',index_col = 0)
data = data.dropna()
data.to_csv('final.csv')
data['comment'].str.contains("bc").astype(int).sum()