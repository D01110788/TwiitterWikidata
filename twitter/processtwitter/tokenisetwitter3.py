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

# Defines the date 15th March 2019 the tweets are considered from
start_time = time.time()
d2 = datetime.datetime(2019, 3, 15)
d22 = datetime.datetime(d2.year, d2.month, d2.day)

# Define the folder directory where the date is extracted to.
here = os.path.dirname(os.path.realpath(__file__))
subdir = "tokenisedtweets3"
load()

# Get the stop words of language English
stopword_set = set(stopwords.words("english"))

# Convert the data time to yyyy/mm/dd
def convert_date_time(dt):
    f = "%Y-%m-%dT%H:%M:%S%fZ"
    dt1 = datetime.datetime.strptime(dt, f)
    dt2 =  datetime.datetime(dt1.year, dt1.month, dt1.day)
    return dt2

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

# Function to validate if a line of text is empty
def isLineEmpty(line):
    return len(line.strip()) < 1 


# Process text removing spaces, comas and quotes
def process_text(text): 
    text = text.lower()
    text = text.replace(',', '')
    text = text.replace('"', '')
    text = text.replace("'", '')
    text = text.replace("  ", ' ')
    # Convert text string to a list of words
    return text.split()
     
# Add quotes to a string
def addQuotes(s1):
    return "'" + s1 + "'"   


counter=0
csv_folder_path = os.path.join("tokenisedtweets2")
# In order to get the list of all files that ends with ".csv"
# we will get list of all files, and take only the ones that ends with "csv"
csv_files = [ x for x in os.listdir(csv_folder_path) if x.endswith("csv") ]
csvdata = list()
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
       
       