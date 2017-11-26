# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 00:07:23 2017

@author: ayesha
"""

from pycorenlp import StanfordCoreNLP
import re
import ast
from nltk.tree import Tree
nlp = StanfordCoreNLP('http://localhost:9000')

def reorder(sentence):
    tag_sen = nlp.annotate(sentence, properties={           #first import the parse tree
  'annotators': 'tokenize,ssplit,pos,depparse,parse',
  'outputFormat': 'json'
  })
    tag_sen = str(tag_sen['sentences'][0]['parse'])
    sen_type = Tree.fromstring(tag_sen)[0].label()          #identify the type of sentence
    #print 'type', sen_type
    
    tag_sen = re.sub('[ \t\n]+', ' ', tag_sen)              #remove any new line and redundant whitespace character
    
    file_name = {'S' : 'declarative.txt', 'SBARQ' : 'interrogative.txt', 'SINV' : 'interrogative.txt'}
    #print file_name[sen_type]
    rule = open(file_name[sen_type])                        #open the respective file
    for line in rule:                                       #reorder according to the rule
        line = line.strip()
        #print line
        key, order = line.split('#')
        key, order = key.strip(), order.strip()
        tag_sen = re.sub(key, order, tag_sen)
        #print tag_sen
    
    #print tag_sen
    tag_sen = re.findall(r'\(\S+ \S+?\)', tag_sen)           #extract all the tags
    #print tag_sen
    tmp_str = ''
    for item in tag_sen:
        tmp_str += item + ','
    tag_sen = tmp_str[: -1]
    tag_sen = tag_sen.replace(' ', '", "')
    tag_sen = tag_sen.replace('(', '("')
    tag_sen = tag_sen.replace(')', '")')
    tag_sen = list(ast.literal_eval(tag_sen))
    #print tag_sen
    return tag_sen, sen_type
    
#print reorder('What were you doing yesterday')
#print reorder('When are you going to school')
#print reorder('I am eating')
