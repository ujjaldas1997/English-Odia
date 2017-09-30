# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:40:24 2017

***It dumps the english words to odia meanings(separated in case a word has more than a odia meaning) and its POS tag
It has been implemented using the syntax tree data structure for python
So the output is not in human readable format
There is a file  eng_odia.txt which has a human readable format of this output.
But this kind of dumping helps in very fast retrieval and thus accessing time 
is very less making it viable for machine translation.***


@author: embis
"""
import cPickle
import SuffixTree.SubstringDict
substring_dict=SuffixTree.SubstringDict()
my_dict=dict()
file1=open("eng_odia.txt","r");
for line in file1:
    line=line.strip()
    #print i
    s=line.split(":")
    s[0]=s[0].strip()
    s[1]=s[1].strip()
    #print s
    eng=s[0]
    odia=s[1]
    odia_list=odia.split(" ")
    if eng not in my_dict.keys():
        my_dict[eng]=odia_list
    else:
        my_dict[eng] += list(set(odia_list)-set(my_dict[eng]))
#print my_dict['abstain']
'''for key,odia_words in my_dict.items():
    substring_dict[key]=odia_words'''
with open('eng_odia_dict.txt','wb') as file2:
    cPickle.dump(my_dict,file2)
        #print eng,odia
    #for j in odia_list:
        #print j
    
    #print type(eng),type(odia),type(odia_list),type(pos)
