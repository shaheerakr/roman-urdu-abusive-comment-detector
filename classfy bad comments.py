# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 20:27:21 2018

@author: Shaheer Akram
"""

import pandas as pd
data = pd.read_csv('final.csv',index_col=0)
data.head()
data['comment'].str.contains('taata').astype(int).sum()
lexicon = 'chut|chod|randi|bharw|bsdk|gand|bhsdk|bhosri|lora|lori|choot|muth|lore|laude|lund|takke|gaand|jhant|dalle|taata'
abusive = data['comment'].str.contains(lexicon)
data['rating'] = abusive
data.head()
abuse = data[data.rating == True]