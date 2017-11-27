# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 23:47:08 2017

@author: ayesha
"""

import json
f=open('verb_root_odia.txt','r')
d = dict()
for line in f:
    eng, odia= line.split(':')
    #print len(line.split(':'))
    #print eng, odia
    eng = eng.strip()
    odia = odia.strip()
    
    d[eng] = odia
#print d
with open('verb_odia.txt','w') as outfile:
    json.dump(d, outfile)
    