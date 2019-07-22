# TwiitterWikidata
Project identifying if a correlation exists between live streamed Twitter hashtags and Wikidata revisions.


# Part 1 Twitter Data Live Streaming  
Part 1 streams live twitter data and stored the results in .json files within the project structure. See website https://www.tweepy.org/ for more details on streaming twitter data.

1. Install visual studio code
2. Create the directory structure C://CC on the machine 
3. Assuming the use has a git account and gitbash installed (if working on windows) clone the project by running 'git clone https://github.com/D01110788/TwiitterWikidata.git' 
4. From the command prompt within Visual Studio Code, run 'pip install tweepy' to install 'tweepy' that required to stream live twitter data.
5. Create a twitter account then open the website http://apps.twitter.com and create a developer app.
6. The consumer keys and tokens are found within the application details page located located at https://dev.twitter.com/apps (found within the "OAuth settings")
7. Add the account specific details for consumer key and secret within the file ssstreaming.py of this project replacing the ****** value key and token with those obtained from twitter app.
   
         consumer_key="***************************"
         consumer_secret="*****************************************"

8. After the step above, you will be redirected to your app's page.
9. Create an access token under the the "Your access token" section.  The access tokens located in the application details page located at  https://dev.twitter.com/apps (found within the "Your access token") 
10. Add access token and secret specific tokens within the file sstreaming.py of this project replacing the ***** value token and secret with those obtained from the twitter app.
11. 
         access_token="*****************************************"
         access_token_secret="****************************************"

12. Navigate to C:\CC\TwiitterWikidata\twitter\streamtwitter
13. Run 'python sstreaming.py
14. The data will be streamed to the folder C:/CC/TwiitterWikidata/twitter/streamtwitter/tweets/. An example of the initial file and overflow file has been added as a sample within the tweets folder of this project. If an error occurs streaming the data the data will auto start again starting with the file 'myprefix.<date-time>.json' and the overflow file 'streamer.<date-time>.json'



# Part 2 Twitter data parsing

Part 2 parses the twitter live streamed data from Part 1 above storing the results within the project structure. This processing includes cleaning of the tweets by extracting the hashtags per tweet removing ASCII characters, removing strings of less than minimum length, splitting in to words, removing stop words of language English and storing the results for additional processing. TThe strings are split in preparation for applying n-grams. N-grams (1 to 4 is applied to the data). For each of the 4 n-gram output the spaces are stripped, hashtag occurrences are counted and ordered by the most frequent for further processing.

1. wordsonly1.py    - FROM  'streamtwitter/tweets' folder   ->   TO 'tweetwords' folder 
* Take the tweets files '.json' format tweets and parses the tweet removing the hashtag, removing non ASKII characters, validating the line contains at least 2 characters and placing the content in the 'tweetwords' folder with file format 'Words_Only.<date>.csv' for additional processing. If the number of words added to the file is greater than or equal to 5000 a new file is created or if the end of the .json file is reached.

2. tokenisetwwitter2.py    -from tweetwords folder /  to tokenisedtweets2 folder
* This process takes the hashtag full words from step 1 splits the word in to individual words based on the 'wordsegment' python implementation, converts the string to lower case, removes stop words using the python implementation 'stopwords' of the English language. The result length is validated greater than 2 and output to a new .csv file 'tokenise.<date-time>.csv' for further processing. 

3. tokenisetwwitter3.py   - from tokenisedtweets2 / to  tokenisetweets3 # break up big ngrams

This implementation breaks up the big n-ngrams. Each line is processed separately - Firstly the line from the .csv file is read, and the sentence length in words is determined where a space indicates a new word. 
  
* If the sentence length is less than 5 (equal to 4 words) print the full text to the new .csv file for further processing.
*  If the sentence length is equal to 5 words split the string in to the first 3 words and the last 2 words and add both to the output file. Then take the first 2 words and last 3 words of the same entry and add them to the output file.
*  If the sentence length is equal to 6 words split the string in to the first 3 words and the last 3 words and add both to the output file. 
* If the sentence length is equal to 7 words split the string in to the first 4 words and the last 3 words and add both to the output file. Then take the first 3 words and last 4 words of the same entry and add them to the output file.
* If the sentence length is equal to 8 words split the string in to the first 4 words and the last 4 words and add both to the output file

4. Apply n-grams (1-grams, 2-grams, 3-grams, 4-grams(no processing required this is the output file from previous step))

* tokeniseengrams1.py - from tokenisetweets3 => to ngrams1 folder  => If the sentence length is equal 1 word add the word to the output file otherwise apply 1-grams to the text and output each word to the output file
* tokeniseengrams2.py  - from tokenisetweets3 => to ngrams2 folder => If the sentence length is less than or equal to 2 word add the word to the output file otherwise apply 2-grams to the text and output each sentence to the output file.
* tokeniseengrams3.py  - from tokenisetweets3 => to ngrams3 folder => If the sentence length is less than or equal to 3 word add the word to the output file otherwise apply 3-grams to the text and output each sentence to the output file.
* tokeniseengrams4.py  - from tokenisetweets3   => to ngrams3 folder => Additional processing not required as 4 ngrams in tokenisetweets3 output file of previous step - execution of tokeniseengrams4.py results in no additional data as the large hashtags were already split in the previous step



5.  Remove spacing from the each of the n-gram output from step 4 before counting occurrences in each of the n-grams
   
* Nothing to do for one words ones 1ngrams   # no change
* removespacesgrams2.py     FROM ngrams2 folder  TO nspacesngram2                    
* removespacesngrams3.py     FROM ngrams3 folder  TO nspacesngram3
* removespacesngrams4.py     FROM tokenisedtweets3 folder  TO nspacesngram4


6. countwordsonly - Count the number of occurrences of each hashtag word to output files

* countwordsonlyngrams1.py     FROM ngrams1 folder  TO ngramscount1 
* countwordsonlyngrams2.py     FROM nspacesngram2 folder  TO ngramscount2
* countwordsonlyngrams3.py     FROM nspacesngram3 folder  TO ngramscount3
* countwordsonlyngrams4.py     FROM nspacesngram4 folder  TO ngramscount4


7. getmaxwords1.py   Orders the twitter results per n-gram folder based on those that occur most frequent

* getmaxwordsngrams1.py   FROM ngramscount1 folder  TO orderedresultsngram1
* getmaxwordsngrams2.py   FROM ngramscount2 folder  TO orderedresultsngram2
* getmaxwordsngrams3.py   FROM ngramscount3 folder  TO orderedresultsngram3
* getmaxwordsngrams4.py   FROM ngramscount4 folder  TO orderedresultsngram4





# Part 3 Wikidata xml revision parsing



1. Download python latest version for windows from here https://www.python.org/downloads/  for example click the yellow button 3.7.3
2. When installing select the checkbox to add to path
3. Select the custom option and then select the location item and add to c:python as the location (navigate to the location but create the folder python in c:/ first)

4. Download pip by running the following from a dos prompt 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
5. Once finished run the following from the same command prompt 'python get-pip.py'

6. Navigate your dos prompt to C:/python/scripts and run 'pip install SPARQLWrapper'
7. Download visual studio code https://visualstudio.microsoft.com/vs/

8. Create a new project folder on your cdrive   C:\CC\TwiitterWikidata and add the subfolders '\wikidata\parsewikidata'
9.  The project python file 'parsexml.py' is added to the project and this will parse the wikidata xml file containing the revision data
10. The parsed data is added to a new additional folder here 'data'
11. Go to this site https://dumps.wikimedia.org/wikidatawiki/<wikidata dump date>/  (the selected date to download the wikidata dumps containing the wikidata metadata revision files)
        Download each wikidata dump xml files for parsing for example wikidatawiki-20190601-stub-meta-history1.xml.gz  
        Select each one and unzip to a location - u will get an xml file  E.G. c:/wikidata/
        Now start visual studio code from your start menu
        On the console you will see add folder - navigate to C:\CC\TwiitterWikidata and open

12. Ready to run the code
13. To run the code select 'terminal - new terminal' on the top menus in visual studio code- this will open a cmd terminal at the bottom of the page
14. Navigate to the location C:\CC\TwiitterWikidata\wikidata\parsewikidata 
15. Enter the command  'python parsexml.py' and run it.
16. You will see number output on the command prompt. This is a print out statement within the code showing the count of the number of revision items processed and can be comment out if not required within the code but validates the xml file is being processed successfully.
17. Additionlly the output for the processed data can be seen in the output witin the data folder .csv file that with 1 row per processed revision located in.  The data output is in the format "'pageid', 'pagetitle',  'label', 'revisionid', 'timestamp', 'comment', 'parentid'"




# Part 4 Wikidata processing


Having completed Part 3 of the process above where data is added to 'data' folder
Next step is to extract the 3rd element from the list - remove the spaces and add to a files

* parsexml10.py            FROM  data  TO    wikidatalabels

* countwikidatawordsonly1.py     FROM wikidatalabels   TO orderedwikidataresults

* getmaxwordswikidata1.py   FROM orderedwikidataresults  TO wikidataprocessed  




# Part 5 Twitter and Wikidata analysis


1. Calculate Jaccards Distance, Jaccards Similarity, kolmogorov-smirnov statistic value and kolmogorov-smirnov p-value


<Initial Execution>
 Retrieve the list of wikidata items returned from Step 4 within the folder wikidataprocessed. The initial list had to be reduced in size because of out of memory exception errors that resulted when running the statistical formula. All wikidata items with a total revisions of greater than three were added to a new list csv file for use when calculating the statistical measures

*  The file statistics.py contains the statistical formula for calculating Jaccards Distance, Jaccards Similarity, kolmogorov-smirnov statistic value and kolmogorov-smirnov p-value 

* Each formula is run per n-grams (1-gram, 2-gram, 3-gram, 4-gram)


* <This process is run for 100%, 50%, 10% and .1% of both the twitter data and wikidata across each of the n-grams (1-gram, 2-gram, 3-gram, 4-gram)> 
* The implementation for each is contained within the folder graphs folders 100, 50, 10, 1 with each of the formula above executed for each group.


2. Graphs / Charts  (TODO://  DOCUMENTING IN PROGRESS)

* This class takes the data output from wikidata processed in Part 4 'wikidataprocessed' and splits the filelds  <name><total> in to 2 fields for the wikidata results in then placed in graphs/wikidatafinal.csv file
* This is run by execution of the command 'python splitdatatofields.py'


Manually create the file as follows  - Take the values in results from the finishing lists from Part 5 - item 1 graphs/wikidatafinal.csv and output from Part 2 item 2 
* wikiandtwitter1.csv  => (column 1) orderedresultsngram1  (column 2) wikidatafinal
* wikiandtwitter2.csv  => (column 1) orderedresultsngram2 (column 2) wikidatafinal
* wikiandtwitter3.csv => (column 1) orderedresultsngram3 (column 2) wikidatafinal
* wikiandtwitter4.csv => (column 1) orderedresultsngram4 (column 2) wikidatafinal


**Statistics for Jaccards ratio charts includes**
* run python jaccardfinal.py   - output to file graphs/jacartadistance1.csv)  => plot this TODO://
* run python jaccardfinal.py   - output to file graphs/jacartadistance2.csv)  => plot this TODO://
* run python jaccardfinal.py   - output to file graphs/jacartadistance3.csv)  => plot this TODO://
* run python jaccardfinal.py   - output to file graphs/jacartadistance4.csv)  => plot this TODO://


**Charts**
* (One list for wikidata (always same)), one list for twitter per ngram list from files ngramschartsFOUR.py, ngramschartsTHREE.PY,ngramsChartsFour.py, ngramschartsONE.py)
* BarChartNGrams1Hashtags.py
* BarChartNGrams2Hashtags.py
* BarChartNGrams1Hashtags.py
* BarChartNGrams1Hashtags.py
* BarChartSummaryTotalsTwitter.py
* BarChartSummaryTotalsWikidata.py
* BarChartWikidataRevisions.py









