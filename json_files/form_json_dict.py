# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:46:42 2017

@author: ayesha
"""

import json

f = open('eng_odia.txt', 'r')
d = dict()
for line in f:
    eng, odia, temp = line.split(':')
    #print len(line.split(':'))
    eng = eng.strip()
    odia = odia.split()
    
    odia = odia[0].strip()
    odia = odia.replace('_', ' ')
    d[eng] = odia
#print d
with open('vocabulary.txt','w') as outfile:
    json.dump(d, outfile)
    