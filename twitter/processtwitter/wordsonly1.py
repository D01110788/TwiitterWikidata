# This file parses the real time streamed live twitter data removing the hashtags from each individual
# tweet created on or after 15th March 2019 and places each tweet work in to a .csv file for further
# processing. The data was collected from 15th March 2019 to 1st June 2019 in this analysis.

# The data set used is available in TODO://

# When the tweet hashtags are extracted fromthe tweet the tweet hashtags are extracted to a folder 
# 'tweetwords' folder with file extension .csv for additional processing.
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

# Define the date tweets are extracted from.
here = os.path.dirname(os.path.realpath(__file__))
subdir = "tweetwords"

# Create a new file
def newfilecreation(filename, articlesWriter):
        print('NEW PROCESS')
        articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)
        articlesWriter.writerow(['hashtagtext'])
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
        filepath = os.path.join(here, subdir, 'Words_Only' + '.' + time.strftime('%Y%m%d-%H%M%S') + '.csv')
        filename=open(filepath, 'w', newline='', encoding="utf-8")
        print(filename)
        print('OPENED')  
        return filename

# Check if the line is empty with a string value of less that 1. This required because when 
# tweets are recorded empty lines are placed between each tweet record added.
def isLineEmpty(line):
    return len(line.strip()) < 1 


# Remove all non letters from the hashtags
ascii_chars = set(ascii_letters)
def remove_non_ascii_prinatble_from_list(list_of_words):
    return [word for word in list_of_words 
            if all(char in ascii_chars for char in word)]

counter=0
json_folder_path = os.path.join('C:/CC/TwiitterWikidata/twitter/streamtwitter/tweets/')
# In order to get the list of all files that ends with ".json"
# we will get list of all files, and take only the ones that ends with "json"
json_files = [ x for x in os.listdir(json_folder_path) if x.endswith("json") ]
json_data = list()
print(json_files)
for json_file in json_files:
    print('#####    NEW FILE ######')
    print(json_file)
    filepath = os.path.join(here, subdir, 'Words_Only' + '.' + time.strftime('%Y%m%d-%H%M%S') + '.csv')
    filename=open(filepath, 'w', newline='', encoding="utf-8")
    articlesWriter = csv.writer(filename, quoting=csv.QUOTE_MINIMAL)
    articlesWriter.writerow(['hashtagtext'])
    hashtagtext = ''
    pathWikiXML = os.path.join(json_folder_path, json_file)
    print('#####    OPEN NEW FILE ######')
    with open(pathWikiXML, 'rb') as f:
        try:
            print('##### TRY ######')
            for line in f:
               if not isLineEmpty(line):
                  tweet = json.loads(line)
                  hashtags = []
                  for hashtag in tweet['entities']['hashtags']:
                       row = (
                           hashtag['text'].lower(),# hashtag
                        )
                       # Original hash tag row
                       values = [(value) for value in row]
                       #Remove non english words
                       values1 = remove_non_ascii_prinatble_from_list(values)

                       if (values1 != []):
                           if counter == 5000:
                                print('YES CREATE NEW FILE')
                                filename = closeoldfile(filename)
                                articlesWriter = newfilecreation(filename, articlesWriter)
                                print('GOT OUT OF CREATED FILE')
                                counter=0
                                #print(filename)
                           writer = csv.writer(filename, delimiter=',')
                           #print(values1)
                           writer.writerow(values1)
                           counter += 1 
                           print(counter)

        except Exception as ex:
               print(ex)
               print(str(ex)) # for just the message
               print(ex.args) # the arguments that the exception has been called with. 
                  # the first one is usually the message.