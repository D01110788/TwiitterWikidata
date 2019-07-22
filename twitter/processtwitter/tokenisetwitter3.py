# This implementation breaks up the big n-ngrams. Each line is processed separately.
# Firstly the line from the .csv file is read, and the sentence length in words is 
# determined where a space indicates a new word. 
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
subdir = "tokenisetweets3"
load()

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

counter=0
csv_folder_path = os.path.join("tokenisedtweets2")
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
                    time.sleep(0.01)
                    print('------------------------------------------------------------------')
                    #print('ORIGINAL VALUES FROM HASHTAG')  
                    
                    #print(line[0])
                    words = line[0].split()    
                    sentanceLength = len(words)               
                    #print(words)
                    print(sentanceLength)
    
                    # ngrams
                    if (sentanceLength < 5):
                        print('LESS THAN 5')
                        writer = csv.writer(filename, delimiter=' ')
                        print(words)
                        writer.writerow(words)
                        counter += 1 

                    elif (sentanceLength == 5):
                        print('5 WORDS')
                        # take the first 3 words and add 
                        firstThreeWords5 = words[:3]
                        writer = csv.writer(filename, delimiter=' ')
                        print(firstThreeWords5)
                        writer.writerow(firstThreeWords5)
                        counter += 1 
                        # take the last 2 words and add 
                        lastTwoWords5 = words[-2:]
                        writer = csv.writer(filename, delimiter=' ')
                        print(lastTwoWords5)
                        writer.writerow(lastTwoWords5)
                        counter += 1 
                        # take the first 2 words and add 
                        firstTwoWords5 = words[:2]
                        writer = csv.writer(filename, delimiter=' ')
                        print(firstTwoWords5)
                        writer.writerow(firstTwoWords5)
                        counter += 1 
                        # take the last 2 words and add 
                        lastThreeWords5 = words[-3:]
                        writer = csv.writer(filename, delimiter=' ')
                        print(lastThreeWords5)
                        writer.writerow(lastThreeWords5)
                        counter += 1 
                    elif (sentanceLength == 6):
                        print('6 WORDS')
                        # take the first 3 words and add 
                        firstThreeWords6 = words[:3]
                        writer = csv.writer(filename, delimiter=' ')
                        print(firstThreeWords6)
                        writer.writerow(firstThreeWords6)
                        counter += 1 
                        # take the last 3 words and add 
                        lastThreeWords6 = words[-3:]
                        writer = csv.writer(filename, delimiter=' ')
                        print(lastThreeWords6)
                        writer.writerow(lastThreeWords6)
                        counter += 1 
                    elif (sentanceLength == 7):
                        print('7 WORDS')
                        # take the first 4 words and add 
                        firstFourWords7 = words[:4]
                        writer = csv.writer(filename, delimiter=' ')
                        print(firstFourWords7)
                        writer.writerow(firstFourWords7)
                        counter += 1 
                        # take the last 3 words and add 
                        lastThreeWords7 = words[-3:]
                        writer = csv.writer(filename, delimiter=' ')
                        print(lastThreeWords7)
                        writer.writerow(lastThreeWords7)
                        counter += 1 
                        # take the first 3 words and add 
                        firstThreeWords7 = words[:3]
                        writer = csv.writer(filename, delimiter=' ')
                        print(firstThreeWords7)
                        writer.writerow(firstThreeWords7)
                        counter += 1 
                        # take the last 4 words and add 
                        lastFourWords7 = words[-4:]
                        writer = csv.writer(filename, delimiter=' ')
                        print(lastFourWords7)
                        writer.writerow(lastFourWords7)
                        counter += 1 
                    elif (sentanceLength == 8):
                        print('8 WORDS')
                        # take the first 4 words and add 
                        firstFourWords8 = words[:4]
                        writer = csv.writer(filename, delimiter=' ')
                        print(firstFourWords8)
                        writer.writerow(firstFourWords8)
                        counter += 1 
                        # take the last 4 words and add 
                        lastFourWords8 = words[-4:]
                        writer = csv.writer(filename, delimiter=' ')
                        print(lastFourWords8)
                        writer.writerow(lastFourWords8)
                        counter += 1 
                    else: print("nothin")

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
       
       