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
subdir = "wikidatalabels"
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

# Process text removing spaces, comas and quotes
def process_text(text): 
    text = text.lower()
    text = text.replace(' ', '')
    text = text.replace('"', '')
    text = text.replace("'", '')
    text = text.replace(".", '')
    text = text.replace("-", '')
    text = text.replace(")", '')
    text = text.replace("(", '')
    text = text.replace(",", '')
    text = text.replace("-", '')
    text = text.replace("Á", '')
    text = text.replace(":", '')
    return text.split()

# Add quotes to a string 
def addQuotes(s1):
    return "'" + s1 + "'"   

# Remove all non letters from the hashtags
ascii_chars = set(ascii_letters)
def remove_non_ascii_prinatble_from_list(list_of_words):
    return [word for word in list_of_words 
            if all(char in ascii_chars for char in word)]

# function to remove stopwords
stopword_set = set(stopwords.words("english"))
def remove_stopwords(sen):    
    sen_new = " ".join([i for i in sen if i not in stopword_set])
    return sen_new


counter=0
csv_folder_path = os.path.join("..\parsewikidata\data")
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
        #print('#####    TRY ######')
        try:
            read = csv.reader(f) 
            next(read)
            for line in read:
                #print(line)
                if (not isLineEmpty(line) and line != []) and not line[0].startswith(',') and line[2] != [] and isinstance(line[2], str):
                    #print('------------------------------------------------------------------')
                    nospaceword = process_text(line[2])   
                    if nospaceword:
                        print(nospaceword)
                        values0 = remove_non_ascii_prinatble_from_list(nospaceword)
                        values1 = remove_stopwords(values0)
                        print(values1)
                        #print('NOSPACEWORD')  
                        #print(len(values1)!=0)
                        if (len(values1)!=0):     
                            writer = csv.writer(filename, delimiter=' ')
                            #print(values1)
                            writer.writerow([values1])
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
       
       