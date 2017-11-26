# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:53:27 2017

@author: ayesha
"""
import re

vowels = r'(A(?:hh|hn|m|n)?|a(?:a|i|u)?|e(?:e)?|i|o(?:o)?|rR(?:r)?|u)'
consonants = r'(B(?:h)?|Ch|D(?:h)?|L|N|R(?:r)?|Sh|T(?:h)?|Y|b(?:h)?|ch|d(?:h)?|g(?:h)?|h|j(?:h)?|k(?:h)?|l|m|n(?:g|y)?|p(?:h)?|r|s(?:h)?|t(?:h)?|v|y)'
letter_code = {
                "~a" : u'\u0B05',
                "~aa" : u'\u0B06',
                "~A" : u'\u0B06',
                "~i" : u'\u0B07',
                "~ee" : u'\u0B08',
                "~u" : u'\u0B09',
                "~oo" : u'\u0B0A',
                "~rR" : u'\u0B0B',
                "~rRr" : u'\u0B60',
                "~e" : u'\u0B0F',
                "~ai" : u'\u0B10',
                "~o" : u'\u0B13',
                "~au" : u'\u0B14',
                "a" : "",
                "aa" : u'\u0B3E',
                "A" : u'\u0B3E',
                "i" : u'\u0B3F',
                "ee" : u'\u0B40',
                "u" : u'\u0B41',
                "oo" : u'\u0B42',
                "rR" : u'\u0B43',
                "rRr" : u'\u0B60',
                "e" : u'\u0B47',
                "ai" : u'\u0B48',
                "o" : u'\u0B4B',
                "au" : u'\u0B4C',
                "k" : u'\u0B15',
                "kh" : u'\u0B16',
                "g" : u'\u0B17',
                "gh" : u'\u0B18',
                "ng" : u'\u0B19',
                "ch" : u'\u0B1A',
                "Ch" : u'\u0B1B',
                "j" : u'\u0B1C',
                "jh" : u'\u0B1D',
                "ny" : u'\u0B1E',
                "t" : u'\u0B1F',
                "T" : u'\u0B20',
                "d" : u'\u0B21',
                "D" : u'\u0B22',
                "N" : u'\u0B23',
                "th" : u'\u0B24',
                "Th" : u'\u0B25',
                "dh" : u'\u0B26',
                "Dh" : u'\u0B27',
                "n" : u'\u0B28',
                "p" : u'\u0B2A',
                "ph" : u'\u0B2B',
                "b" : u'\u0B2C',
                "v" : u'\u0B2C',
                "bh" : u'\u0B2D',
                "B" : u'\u0B2D',
                "Bh" : u'\u0B2D',
                "m" : u'\u0B2E',
                "y" : u'\u0B2F',
                "r" : u'\u0B30',
                "l" : u'\u0B32',
                "L" : u'\u0B33',
                "sh" : u'\u0B36',
                "Sh" : u'\u0B37',
                "s" : u'\u0B38',
                "h" : u'\u0B39',
                "R" : u'\u0B5C',
                "Rr" : u'\u0B5D',
                "Y" : u'\u0B5F',
                "Ahn" : u'\u0B01',
                "Am" : u'\u0B02',
                "Ahh" : u'\u0B03',
                "An" : u'\u0B3C',
                "~Ahn" : u'\u0B01',
                "~Am" : u'\u0B02',
                "~Ahh" : u'\u0B03',
                "~An" : u'\u0B3C',
                "*" : u'\u0B4D'
                }

regex = vowels[:-1] + '|' + consonants[1:]
def phonetics(inp):
    inp = inp.lower()
    regex = vowels[:-1] + '|' + consonants[1:]
    #print regex
    #inp = 'se' #'suresh'
    words = inp.strip().split()               #analyse for each word
    output = ''
    for word in words:
        form = re.split(regex, word)
        form = filter(None, form)              #filter out all the empty values
        #print form
        if re.search(vowels, form[0]):         #check if vowel is present at the beginning
            form[0] = '~' + form[0]
        if re.search(consonants, form[-1]):    #check if consonant is present in the end
            form.append('*')
        out = ''
        for it in range(len(form)):
            if form[it] in letter_code:
                out += letter_code[form[it]]          #check if a particular key is available in dictionary
            else:
                out += form[it]                       #else print as it is
            try:
                if re.search(consonants, form[it]) and re.search(consonants, form[it + 1]):
                    out += letter_code['*']
            except:
                pass
            
        output += out + ' '                    #add a space after each word
    return output
    #print list(output)
#print phonetics('chh')