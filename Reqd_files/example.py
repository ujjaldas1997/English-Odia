#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 01:03:18 2017

@author: akankshya
"""

from util import reorder
import re
##print reorder('What were you doing yesterday')
##print reorder('When are you going to school')
l= reorder('i was going to school')
#print l
output = [l[0]]
for item in l:
    if re.search(r'(?:VB|MD)', item[0]):
        output.append(item)
        
print output
#output = filter(output, None)
#print output
def ret_out():
    return output
