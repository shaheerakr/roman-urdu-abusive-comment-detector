# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 20:27:21 2018

@author: Shaheer Akram
"""

import pandas as pd
data = pd.read_csv('final.csv',index_col=0)
data.head()
data['comment'].str.contains(lexicon).astype(int).sum()
yasir = 'bhosda|chut|chod|chinaal|gaandu|randi|gaandfat|takke|bhenchod|bharw|khotey|lauda|kutta|taata|bdsk|bharwa|gaand|lassan|choot|maderchod|laude|ullu|chhed|bhosri|lora|kutte|bhadwe|lore|gand|randi|cuntmama|bsdk|gaandu|betichod|bhosadike|lund|rundi|bhen|kutte|hijra|chodu|chunni|jhant|dalle|tatti|mader|paad|kamina|tatay|bhsdk|gadha|bhen|kuttiya|lori|jhaat|chutiya|gandu|choot|lund|gaand|muth|gaand|moot|chut|taatay|marani|bhadhava|bhonsri|jhaant|chuda|kutti'
lexicon = 'chut|chod|chood|bhosda|bhosadike|rundi|jhand|jhaant|madr|bhadhava|madar|mader|bhonsri|randi|bharw|bsdk|gand|bhsdk|bhosri|lora|lori|choot|muth|lore|laude|lund|takke|gaand|jhant|dalle|taata'
data['rating'] = data['comment'].str.contains(lexicon)
data.to_csv('labeled.csv')
data.head()
abuse = data[data.rating == True]