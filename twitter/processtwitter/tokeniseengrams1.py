# This class applies n-grams (1-grams) to the data from the data located in the folder tokenisetweets3 where the output
# is stored in the folder ngrams1. If the sentence length is equal 1 word add the word to the output file otherwise 
# apply 1-grams to the text and output each word to the output file
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
subdir = "ngrams1"
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

#Function to validate min length of line is greater than 2
def isMinLengthLine(line):
    return len(line.strip()) > 2

# Process text removing spaces, comas and quotes
def process_text(text): 
    text = text.lower()
    text = text.replace(',', '')
    text = text.replace('"', '')
    text = text.replace("'", '')
    return text.split()

counter=0
csv_folder_path = os.path.join("tokenisetweets3")
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
        print('#####    TRY ######')
        try:
            read = csv.reader(f) 
            next(read)
            for line in read:
                #print('START')
                #print(line)
                if (line != []):
                    print('------------------------------------------------------------------')
                    words = line[0].split()    
                    sentanceLength = len(words)               
                    print(sentanceLength)
                    myData = ' '.join(words)
                    # ngrams
                    if (words and isMinLengthLine(line[0])):
                        time.sleep(0.01)
                        if counter >= 5000:
                            print('YES CREATE NEW FILE')
                            filename = closeoldfile(filename)
                            articlesWriter = newfilecreation(filename, articlesWriter)
                            print('GOT OUT OF CREATED FILE')
                            counter=0
                        if (sentanceLength == 1):
                            print('1 word')
                            writer = csv.writer(filename, delimiter=' ')
                            print(words)
                            writer.writerow(words)
                            counter += 1 
                        else:
                            print('More than 1 word')
                            print(myData)
                            print('######')
                            n = 1
                            oneGrams = ngrams(myData.split(' '), n)
                            for grams in oneGrams: 
                                print(grams)
                                gramsItem = [' '.join(grams)]
                                print(gramsItem)
                                gramsItem
                                writer = csv.writer(filename, delimiter=' ')
                                writer.writerow(process_text(' '.join(gramsItem)))
                                counter += 1

        except Exception as ex:
               print(ex)
               print(str(ex)) # for just the message
               print(ex.args) # the arguments that the exception has been called with. 
                  # the first one is usually the message.
       
       