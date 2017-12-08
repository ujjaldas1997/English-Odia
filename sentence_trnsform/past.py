'''import nltk
#from example import ret_out
from nltk import regexp_tokenize
#sent="I was eating"'''
from stem_verb import stem_verb as sb
from phonetics import phonetics as ph
def get_verb(l):
    suf=''
    #text=regexp_tokenize(sent,"[\w']+")
    #text=[('PRP', 'I'), ('VBG', 'going'), ('VBD', 'was')]
    #print text
    #print nltk.pos_tag(text)
    #l=[('PRP', 'I'), ('VBG', 'eating'), ('VBN', 'been'), ('VBD', 'had')]
    
    
    #text=ret_out()
    c=0
    max1=0
    s=''
    #print len(text)
    for i in range(0,(len(l))):
        x=l[i][0]
        r={"VBD":1,
           "VBD":2,
           "VBG":2,
           "VBN":3,
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
      }
    if y in s:
        k2=s[y]
    else :
        k2=4
    k1=max1  
    if(k2==1):
        if(k1==2 and c==1):
            suf="eechhi"
        elif(k1==2 and c==2):
            suf="uuthhili"
        elif(k1==3 and c==3):
            suf="eeaasutthili"
        elif(k1==3):
            suf="eethhili"
    if(k2==2):
        if(k1==1 and c==1):
            suf="uuchhu"
        elif(k1==2 and c==2):
            suf="uuthhile"
        elif(k1==3 and c==3):
            suf="eeaasutthile"
        elif(k1==3):
            suf="eethhile"
    if(k2==3):
        if(k1==1 and c==1):
            suf="uuchha"
        elif(k1==2 and c==2):
            suf="uuthhila"
        elif(k1==3 and c==3):
            suf="eeaasutthila"
        elif(k1==3):
            suf="ithhila"
    if(k2==4):
        if(k1==2 and c==1):
            suf="ichhee"
        elif(k1==2 and c==2):
            suf="uuthhilaa"
        elif(k1==3 and c==3):
            suf="aasutthilaa"
        elif(k1==3):
            suf="ithhilaa" 
    if(k2==5):
        if(k1==2 and c==1):
            suf="ichhanthi"
        elif(k1==2 and c==2):
            suf="uuthhile"
        elif(k1==3 and c==3):
            suf="aasutthile"
        elif(k1==3):
            suf="ithhile"
    #print c 
    #print k1
    
    if c==1:
         for i in range(0,(len(l))):
                if(l[i][0]=='VBD'):
                    s=sb(l[i][1]) 
    elif c==2 and k1==3 :  
        #print 111
        for i in range(0,(len(l))):
            if(l[i][0]=='VBN'):
                s=sb(l[i][1]) 
    else:
        for i in range(0,(len(l))):
            if(l[i][0]=='VBG'):
                s=sb(l[i][1]) 
    #print s, type(s)
    s=ph(s)
    #print s
    suf=ph(suf)
    #print suf
    
    try:
        s=s[:-1]+suf
    except:
        s = suf
    #print s
    return s,c          
    '''
    #print s   
    s=s+suf
    #print s
    return s ,c                              
#print get_verb([('PRP', 'I'), ('VBN', 'gone'), ('VBD', 'had')])
    '''
#wt,c=get_verb([('PRP', 'I'), ('VBN', 'gone'), ('VBD', 'had')])
#print wt