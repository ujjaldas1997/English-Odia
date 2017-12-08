# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:28:14 2017

@author: ayesha
"""

#import nltk
#from nltk import regexp_tokenize
#sent="She will eat"
suf=''
#text=regexp_tokenize(sent,"[\w']+")
#print text, type(text)
#l=[('PRP', 'I'), ('MD', 'will'), ('VBG', 'going'), ('VB', 'be')]
#print l, type(l[0])
from stem_verb import stem_verb as sb
from phonetics import phonetics as ph
def get_verb(l):
    c=0
    #print len(text)
    max1=0
    for i in range(0,(len(l))):
        x=l[i][0]
        p={
            "MD":1,
            "VB":2,
            "VBG":3,
            "VBN":4,
        }
        if x in p:
            c=c+1
            k1=p[x]
            if(k1>max1):
                max1=k1
        s={
            "I":1,
            "We":2,
            "You":3,
            "She" or "He":4,
            "They":5,
          }
    y=l[0][1]
    if y in s:
        k2=s[y]
    else:
        k2=4

    k1=max1   
        #print "11111"
    if(k2==1):
        if( c==2):
            suf="ibi"
        elif(k1==3 and c==3):
            suf="uuthibi"
        elif(k1==4 and c==3):
            suf="isaarithibi"
        elif(c==4):
            suf="aasuutheebi"
    if(k2==2 or k2==3):
        if( c==2):
            suf="ibu"
        elif(k1==3 and c==3):
            suf="uuthhibu"
        elif(k1==3 and c==3):
            suf="isaarithibu"
        elif(c==4):
            suf="iaasuthibu"
    
    if(k2==4):
        if( c==2):
            suf="iba"
        elif(k1==3 and c==3):
            suf="uuthhiba"
        elif(k1==3 and c==3):
            suf="isaarithiba"
        elif(c==4):
            suf="iaasuthiba"
    if(k2==5):
        if( c==2):
            suf="ibe"
        elif(k1==3 and c==3):
            suf="uuthhibe"
        elif(k1==3 and c==3):
            suf="isaarithibe"
        elif(c==4):
            suf="iaasuthibe"
            
    if(c==2):
        for i in range(0,(len(l))):
            if(l[i][0]=='VB'):
                #print 11111
                s=sb(l[i][1]) 
    elif (c==3 and k1==4):
        for i in range(0,(len(l))):
            if(l[i][0]=='VBN'):
                #print 2222
                s=sb(l[i][1]) 
    else:
        for i in range(0,(len(l))):
            if(l[i][0]=='VBG'):
                #print 3333
                s=sb(l[i][1]) 
                
    #print s
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
    #print s           
    s=s+suf  
    #print c       
    return s,c                       #jaa is only added here
#w,c= get_verb([('PRP', 'I'), ('MD', 'will'), ('VBG', 'going'), ('VB', 'be')])    
#print w   