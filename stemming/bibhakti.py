
'''import nltk
from nltk import regexp_tokenize
import re'''
from phonetics import phonetics
def bibhakti(r):
    #x=raw_input('enter input ')
    r=r.lower()
    inp=''
    p={"he" or 'she':"se",
       'i' :'mu',
       'we':'aame',
       'our':'aamara',
       'my': 'mora',
       'him' or 'her' or 'his':'thaa',
        'they':'se'+ 'maane',
        'them':'thaanka',
        'with':'sahitha',
        'by':'dhbaaraa',
        'to':'ku',
        'for':'nimanthe' ,
        'from':'Taaru',
        'of':'ra',
        'in':'re',
        'on':'upare',
        'among':'gahaNare',
        'between':'bhithare',
        'your':'aapanangkara',
        'their':'thaankara',
        'when':'kebe',
        'where':'kauuthhi',
        'why':'kaahinki',
        'you':'thame'
    }
    if r in p :
        inp=p[r]
    else :
        inp=r
        
        #print inp    
    return phonetics(inp)


#sent="home"
#rint bibhakt(sent)
