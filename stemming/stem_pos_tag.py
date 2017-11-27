import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer  #stemming and lemmatizing
from nltk import regexp_tokenize                     	#tokenize
import pandas as pd
import csv

wr=open("stemmed_words.txt","wr")			#write to stemmed word text file
with open('words_alpha.csv', 'r') as csvfile:		#read from csv file
     data = csv.reader(csvfile, delimiter=' ')
     print data
     stemmer1=PorterStemmer()				#porterStemmer
     lemma=WordNetLemmatizer()				#lemmatizer
     for row1 in data:
        #print (row1)
        row1=row1[0].replace('\n','')			#replace occurence of new line with nochar 
        x=stemmer1.stem(row1)
        y=lemma.lemmatize(row1)
        row1=regexp_tokenize(row1,"[\w']+")		#tokenizing
        z=nltk.pos_tag(row1)				#pos_tagging
        #print row1
        print z[0][0],z[0][1],x ,y#,z'''
        wr.write(z[0][0]+" "+z[0][1]+" "+x+" "+y+'\n')	#writing
csvfile.close()						#closing files
wr.close()
