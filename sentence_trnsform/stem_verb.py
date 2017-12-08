# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 00:03:59 2017

@author: ayesha
"""

from nltk.stem import PorterStemmer
import json
def stem_verb(p):
    st=PorterStemmer()
    s=st.stem(p)
    #print s
    corpus=json.load(open('verb_odia.txt','r'))
    if s in corpus:
        #print s
        return corpus[s]
#print stem_verb('congratulating')