# English to Odia Textual Data Translation
English, being the universal language, the sole aim of Machine Tanslation has been to translate English into various other languages. Indian languages like Hindi, Bengali, Marathi, Tamil and Telugu have been machine translated from English by Google. Unfortunately, Odia has not been machine translated. 
## Requirement
- Python 2.7.x
- Ubuntu 16.04(Tested)
- Jupyter Notebook
- Stanford CoreNLP
### Python modules used(all in latest version)
- BeautifulSoup
- requests
- linecache
- nltk
- pycorenlp
- pandas
### How to start StanfordCoreNLP server
First download the latest version of the same from the [link](http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip) and extract it.  
Now type `ctrl + alt + t` and go to the folder StanfordCoreNLP(in my case it is `cd /home/ujjaldas223/Stanford_Parser/stanford-corenlp-full-2016-10-31`)
My folder structure looks like:  
home  
--ujjaldas223  
----Stanford_Parser  
------stanford-corenlp-full-2016-10-31  
Now paste the following in terminal:  
`java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,parse,depparse -port 9000 -timeout 15000`  
That wil look like  ![txt](https://raw.githubusercontent.com/ujjaldas1997/English_Odia-Translation/master/Screenshot.png)
If you are facing error related to java, update jdk
## How to use :
- Start StanfordCoreNLP server(Description provided above)
- Go to folder `sentence_trnsform`
- Open the file `verb_extract1.py`
- Run the file to see output
Example  ![txt](https://raw.githubusercontent.com/ujjaldas1997/English_Odia-Translation/master/screenshot.jpg)
