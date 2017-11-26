#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:44:31 2017

@author: jijnasa
"""
'''
import nltk
from nltk import regexp_tokenize
sent="She eats"
suf=''
l=regexp_tokenize(sent,"[\w']+")
print l
print nltk.pos_tag(l)
'''
from stem_verb import stem_verb as sb
from phonetics import phonetics as ph
def get_verb(l): 
    #stemmer1=PorterStemmer()
    suf=''
    c=0
    k1=0
    max1=0
    #print len(l)
    for i in range(0,(len(l))):
        x=l[i][0]
        r={"VBZ":1,
           "VBP":2,
           "VBG":3,
           "VBN":4,
        
        }
        if x in r:
            c=c+1
            k1=r[x]
            if(k1>max1):
                max1=k1
    
    y=l[0][1]
    y=y.lower()
    s={
        "i":1,
        "we":2,
        "you":3,
        "she":4,
        "he":4,
        "they":5,
        " ":5,
      }
    if y in s:
        #print 111
        k2=s[y]
    
    k1=max1
    #print c,k1,k2
    if(k2==1):
        if(k1==2):
            suf="e"
        elif(k1==3 and c==2):
            suf="uchhi"
        elif(k1==4 and c==3):
            suf="i"+"asuchhi"
        elif(k1==4 and c==2):
            suf="ichhi"
    if(k2==2):
        if(k1==2):
            suf="uu"
        elif(k1==3 and c==2):
            suf="uchhu"
        elif(k1==4 and c==3):
            suf="iasuchhu"
        elif(k1==4 and c==2):
            suf="ichhu"
    if(k2==3):
        #print 22111
        if(k1==2):
            suf="a"
        elif(k1==3 and c==2):
            #print 2222
            suf="uuchh"
        elif(k1==4 and c==3):
            suf="iasuchha"
        elif(k1==4 and c==2):
            suf="ichha"
    if(k2==4):
        if(k1==1):
            suf="ae"
        elif(k1==3 and c==2):
            suf="uchhi"
        elif(k1==4 and c==3):
            suf="iasuchhi"
        elif(k1==4 and c==2):
            suf="ichhi" 
    if(k2==5):
        if(k1==2):
            suf="aannnti"
        elif(k1==3 and c==2):
            suf="uuchhanthi"
        elif(k1==4 and c==3):
            suf="iasuchhanti"
        elif(k1==4 and c==2):
            suf="ichhanti"
    
    if(c==1):
        if(k2==4):
            for i in range(0,(len(l))):
                if(l[i][0]=='VBZ'):
                    s=l[i][1] 
        else:
            for i in range(0,(len(l))):
                if(l[i][0]=='VBP'):
                    s=l[i][1] 
    elif c==2 and k1==4:
        for i in range(0,(len(l))):
                if(l[i][0]=='VBN'):
                    s=l[i][1]
    else:
        for i in range(0,(len(l))):
                if(l[i][0]=='VBG'):
                    s=l[i][1] 
    #print s
    s=sb(s)
    s=ph(s)
    #print s
    suf=ph(suf)
    #print suf
    
    try:
        s=s[:-1]+suf
    except:
        s = suf
    #print s
    return s ,c     
    '''                
    #print s
    s=sb(s)
    try:
        s=s+suf
    except:
        s = suf
    #print s
    return s ,c                              #khaa added
#print get_verb([('PRP', 'I'), ('VBN', 'gone'), ('VBP', 'have')])
    '''