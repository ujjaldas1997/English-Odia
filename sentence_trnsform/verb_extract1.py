# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:20:52 2017

@author: ayesha
"""
from util import reorder
import json
from past import get_verb as get_past_verb
from future import get_verb as get_future_verb
from present_tense import get_verb as get_present_verb
from bibhakti import bibhakti
from phonetics import phonetics
import re
inpt='We congratulate on your anniversary'
print inpt
l,sen_tag= reorder(inpt)
print l
#print 222
output = [l[0]]
for item in l:
    if re.search(r'(?:VB|MD)', item[0]):
        output.append(item)

#tense = {'VBD', 'MD', 'VBP' or 'VBZ'}
#print 111
#print output
for item in output:
    if item[0]=='VBD':
        p,c=get_past_verb(output)
        break
    elif item[0]=='MD':
        p,c=get_future_verb(output)
        break
    elif item[0]=='VBP' or item[0]=='VBZ':
        #print 111
        p,c=get_present_verb(output)
        break
        
#print p
l = l[:-c]
l.append(p)
#print l
corpus = json.load(open('vocabulary.txt'))
for it in range(len(l)):
    if type(l[it]) is tuple:
        if l[it][0] in {'PRP', 'PRP$', 'IN', 'TO','WRB'}:
            l[it] = bibhakti(l[it][1])
        else:
            #dict
            if l[it][1] in corpus:
                l[it] = corpus[l[it][1]]
            else :
                l[it] = phonetics(l[it][1])
            
    #else:
     #   l[it] = phonetics(l[it])
    
#for item in l:
#    print item
if(sen_tag=='SINV'):
    l.append(phonetics('ki'))
print ' '.join(l)