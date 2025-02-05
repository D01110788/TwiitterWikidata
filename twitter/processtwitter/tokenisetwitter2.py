# This process takes the hashtag full words, splits the word in to individual words based on the
# 'wordsegment' python implementation, converts the string to lower case, removes stop words 
# using the python implementation 'stopwords' of the English language. The result length is 
# validated greater than 2 and output to a new .csv file 'tokenise.<date-time>.csv' for 
# further processing.

import xml.etree.ElementTree as etree
import os
import string
from string import ascii_letters
import io
import re
import csv
import codecs
import datetime
import json, time, sys
import xml.etree.ElementTree as etree
from SPARQLWrapper import SPARQLWrapper, JSON
import wordsegment
from wordsegment import load, segment
import splitter
import enchant, sys
import nltk, re, pprint
from nltk import word_tokenize
#from wordsegmentation import WordSegment
from nltk import ngrams
from nltk.corpus import stopwords


# Define the folder directory where the date is extracted to.
here = os.path.dirname(os.path.realpath(__file__))
subdir = "tokenisedtweets2"
load()

# Get the stop words of language English
stopword_set = set(stopwords.words("english"))


# Create a new file
def newfilecreation(filename, articlesWriter):
        print('NEW PROCESS')
        articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)
        articlesWriter.writerow(['words'])
        return articlesWriter


# Close current file and create new file of type .csv that contains the hashtag words
# A sleep of 5 seconds has been added to allow time for one file to close and the next 
# writable file to be created
def closeoldfile(filename):
        print(filename)
        filename.flush()
        filename.close()
        time.sleep(5)
        print('SLEEPING')     
        filepath = os.path.join(here, subdir, 'tokenise' + '.' + time.strftime('%Y%m%d-%H%M%S') + '.csv')
        filename=open(filepath, 'w', newline='', encoding="utf-8")
        print(filename)
        print('OPENED')  
        return filename

# Check the line content length contains at least 2 characters
def isMinLengthLine(line):
    return len(line.strip()) > 2
    

def process_text(text): 
    text = text.lower()
    text = text.replace(',', '')
    text = text.replace('"', '')
    text = text.replace("'", '')
    text = text.replace("  ", ' ')
    return text.split() 

# Function to remove stopwords
def remove_stopwords(sen):    
    sen_new = " ".join([i for i in sen if i not in stopword_set])
    return sen_new



counter=0
csv_folder_path = os.path.join("tweetwords")
# In order to get the list of all files that ends with ".csv"
# we will get list of all files, and take only the ones that ends with "csv"
csv_files = [ x for x in os.listdir(csv_folder_path) if x.endswith("csv") ]
csv_data = list()
print(csv_files)
for csv_file in csv_files:
    print('#####    NEW FILE ######')
    print(csv_file)
    filepath = os.path.join(here, subdir, 'tokenise' + '.' + time.strftime('%Y%m%d-%H%M%S') + '.csv')
    filename=open(filepath, 'w', newline='', encoding="utf-8")
    articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)
    articlesWriter.writerow(['words'])
    words = ''
    pathWikiXML = os.path.join(csv_folder_path, csv_file)
    print('##### OPEN NEW FILE ######')
    with open(pathWikiXML, 'r') as f:
        print('##### TRY ######')
        try:
            read = csv.reader(f) 
            next(read)
            for line in read:
                #print('START')
                #print(line)
                if (line != []):
                    print('------------------------------------------------------------------')
                    print('ORIGINAL VALUES FROM HASHTAG')                    
                    print(line[0])
                    #print(repr(line[0]))
                    print('SPLITTER ONE')
                    #values1 = splitter.split(line[0])
                    #print(values1)    
                    print('SPLITTER TWO BETTER RESULTS')
                    values0= wordsegment.segment(repr(line[0]))
                    print(values0)

                    #################################
                    ## Add function here to remove stop words 
                    clean_sentences = [s.lower() for s in values0]
                    #print(clean_sentences)
                    values2 = [remove_stopwords(r.split()) for r in clean_sentences]
                    print(values2)
                    values2[:] = [item for item in values2 if item != '']
                    print(values2)
                    print('##################################')
                    #print(clean_sentences)
                    # REQUIRED TO PUT THIS IN IN ORDER FOR FULL FILE TO PROCESS ??
                    time.sleep(0.25)

                    #values2= process_text(values2)
                    sentanceLength = len(values2)
                    #print(sentanceLength)
                    myData = ' '.join(values2)
                    print(myData)
                    print('------------------------------------------------------------------')
                
                    if (values2 and isMinLengthLine(myData)):
                        writer = csv.writer(filename, delimiter=' ')
                        print(values2)
                        writer.writerow(values2)
                        counter += 1 
                        if counter >= 5000:
                            print('YES CREATE NEW FILE')
                            filename = closeoldfile(filename)
                            articlesWriter = newfilecreation
                            (filename, articlesWriter)
                            print('GOT OUT OF CREATED FILE')
                            counter=0

        except Exception as ex:
               print(ex)
               print(str(ex)) # for just the message
               print(ex.args) # the arguments that the exception has been called with. 
                  # the first one is usually the message.
       
       