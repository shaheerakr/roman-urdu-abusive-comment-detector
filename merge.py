# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:25:17 2018

@author: Shaheer Akram
"""

import pandas as pd
import csv
import re
import glob

frames = []
files = glob.glob('*.csv')
for names in files:
    df = pd.read_csv(names)
    frames.append(df)
merge = pd.concat(frames)
del merge['hasReplies']
del merge['numberOfReplies']
merge['commentText'] = merge['commentText'].map(str) + merge['replies.commentText'].map(str)
del merge['replies.commentText']
merge.head()
merge.to_csv("all.csv")
data = pd.read_csv('all.csv',index_col = 0)         #for first ittration
corpus = []             #for every ittration only
X = data['comment']     #for first ittration only
for i in range(len(X)):
    #review = re.sub('nan',' ',str(X[i]))           #remove nan
    #review = re.sub('http\S+',' ',str(X[i]))       #remove links
    review = re.sub('[^a-zA-Z]',' ',str(X[i]))      #remove emojis and punctuations
    review = review.lower()         #run this for last ittration only
    review = review.split()
    review = ' '.join(review)
    corpus.append(review)
    print(i)
clean = pd.DataFrame(corpus)
clean.columns = ['comment']
#clean['comment'].str.contains("https").astype(int).sum()
X = clean['comment']        #from second ittration
clean.to_csv("clean.csv")
data = pd.read_csv('clean.csv',index_col = 0)
data = data.dropna()
data.to_csv('final.csv')
data['comment'].str.contains("bc").astype(int).sum()
clean = pd.read_csv('clean.csv')
clean1 = pd.read_csv('clean1.csv')
clean2 = pd.read_csv('clean2.csv')
clean3 = pd.read_csv('clean3.csv')
clean4 = pd.read_csv('clean4.csv')
clean5 = pd.read_csv('clean5.csv')
clean6 = pd.read_csv('clean6.csv')
data = pd.concat([clean,clean1,clean2,clean3,clean4,clean5,clean6])
data.to_csv('all_clean.csv')