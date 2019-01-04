# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:12:20 2019

@author: Shaheer Akram
"""

import pandas as pd

data = pd.read_csv('final.csv')
data = data[data.comment.str.len() > 15]
len(data[data.rating == True])
data = data['comment'].drop_duplicates()
data = pd.DataFrame(data)
data_false4 = data[data.rating == False]
data_true4 = data[data.rating == True]
merge_true = pd.concat([data_true1,data_true2,data_true3,data_true4])
merge_true.to_csv('galiyan.csv')
data = pd.read_csv('labeled.csv')
del data['Unnamed: 0']
merge_true = pd.read_csv('galiyan.csv')
del merge_true['Unnamed: 0']
merge_false = pd.concat([data_false1,data_false2,data_false3,data_false4])
merge_false.to_csv('no galiyan.csv')
merge_false = pd.read_csv('no galiyan.csv')
del merge_false['Unnamed: 0']
from sklearn.model_selection import train_test_split
X_train,data_false4_splice,y_train,y_test = train_test_split(data_false4.comment,data_false4.rating,test_size = 0.05)
data_false4_splice = data_false4_splice[:28952]
data_false4_splice = pd.DataFrame(data_false4_splice)
data_false4_splice['rating'] = y_test
final_false = pd.concat([data_false4_splice,data_false3_splice,data_false1,data_false2])
dataset = pd.concat([final_false,merge_true])
dataset.to_csv('dataset.csv')

