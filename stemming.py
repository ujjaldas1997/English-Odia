# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#As nltk.tag.pos_tag accept a list of tokens then separate and t
#ags its elements you can not get the tag for one word, instead you can put it within a list then you'll have :
import nltk
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk import pos_tag
#from nltk.tokenize import word_tokenize

stemmer=PorterStemmer()
lemma=WordNetLemmatizer()
f1=open("test1.txt","r")
f2=open("testres1.txt","w+")
'''s="Bringing me the dead people alive and alike."'''
#tokens=nltk.word_tokenize(f1)
for i in f1:
    i = i.replace('\n', '')
    #print i
    i_pos=nltk.tag.pos_tag([i])
    l=list(i_pos[0][1])
    #print l
    q=str.lower(l[0])
    #print q
    if q=='j':
        q=q.replace('j','a')
    '''elif q=='i':
        q=q.replace('i','n')
    elif q=='c':
        q=q.replace('c','n')
    elif q=='m':
        q=q.replace('m','n')
    elif q=='p':
        q=q.replace('p','n')
    elif q=='w':
        q=q.replace('w','n')
    elif q=='t':
        q=q.replace('t','n')'''
    if q=='d':
        continue
    print i,i_pos[0][1],stemmer.stem(i),lemma.lemmatize(i,pos=q)
    f2.write(i)
    f2.write(" ")
    f2.write(i_pos[0][1])
    f2.write(" ")
    f2.write(stemmer.stem(i))
    f2.write(" ")
    f2.write(lemma.lemmatize(i,pos=q))
    f2.write("\n")
f2.close()
f1.close()