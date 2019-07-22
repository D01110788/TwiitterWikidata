import xml.etree.cElementTree as ET
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
subdir = "nspacesngram2"
load()

# Create a new file
def newfilecreation(filename, articlesWriter):
        print('NEW PROCESS')
        articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)
        articlesWriter.writerow(['labels'])
        return articlesWriter

# Close current file and create new file of type .csv that contains the hashtag words
# A sleep of 5 seconds has been added to allow time for one file to close and the next 
# writable file to be created
def closeoldfile(filename):
        #if counter ==10:
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

# Function to validate if a line of text is empty
def isLineEmpty(line):
    return len(line[0].strip()) < 1 

# Replace spaces with empty string
def process_text(text): 
    text = text.replace(' ', '')
    return text.split()
     

counter=0
csv_folder_path = os.path.join("ngrams2")
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
    articlesWriter.writerow(['labels'])
    labels = ''
    pathWikiXML = os.path.join(csv_folder_path, csv_file)
    print('##### OPEN NEW FILE ######')
    with open(pathWikiXML, 'r', encoding='utf-8') as f:
        print('#####    TRY ######')
        try:
            read = csv.reader(f) 
            next(read)
            for line in read:
                print(line)
                if (not isLineEmpty(line) and line != []):
                    print('------------------------------------------------------------------')
                    nospaceword = process_text(line[0])   
                    print(nospaceword)
                    if nospaceword:
                        myData = ' '.join(nospaceword)
                        print('MYData')
                        print(myData)
                        writer = csv.writer(filename, delimiter=' ')
                        print(myData)
                        writer.writerow([myData])
                        counter += 1 
                        time.sleep(0.01)
                    else: 
                        print("empty")
                    if counter >= 5000:
                        print('YES CREATE NEW FILE')
                        filename = closeoldfile(filename)
                        articlesWriter = newfilecreation(filename, articlesWriter)
                        print('GOT OUT OF CREATED FILE')
                        counter=0
        except Exception as ex:
               print(ex)
               print(str(ex)) # for just the message
               print(ex.args) # the arguments that the exception has been called with. 
                  # the first one is usually the message.
       
       