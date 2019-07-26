# TwitterWikidata
Project identifying if a correlation exists between live streamed Twitter hashtags and Wikidata revisions.
**For each step in the process only a sample result output file has been provided of the data content. Due to the large number and size of files the full data content per step could not be included in the project content in Git**


# Part 1 Twitter Data Live Streaming  

Part 1 streams live twitter data and stored the results in .json files within the project structure. See website https://www.tweepy.org/ for more details on streaming twitter data.

1. Install visual studio code
2. Create the directory structure C://CC on the machine 
3. Assuming the use has a git account and gitbash installed (if working on windows) clone the project by running 'git clone https://github.com/D01110788/TwiitterWikidata.git' 
4. From the command prompt within Visual Studio Code, run 'pip install tweepy' to install 'tweepy' that is required to stream live twitter data.
5. Create a twitter account, then open the website http://apps.twitter.com and create a developer app.
6. The consumer keys and tokens are found within the application details page located located at https://dev.twitter.com/apps (found within the "OAuth settings")
7. Add the account specific details for consumer key and secret within the file ssstreaming.py of this project replacing the ****** value key and token with those obtained from twitter app.
   
         consumer_key="***************************"
         consumer_secret="*****************************************"

8. After the step above, you will be redirected to your app's page.
9. Create an access token under the the "Your access token" section.  The access tokens located in the application details page located at  https://dev.twitter.com/apps (found within the "Your access token") 
10. Add access token and secret specific tokens within the file sstreaming.py of this project replacing the ***** value token and secret with those obtained from the twitter app.
    
         access_token="*****************************************"
         access_token_secret="****************************************"

11. Navigate to C:\CC\TwiitterWikidata\twitter\streamtwitter
12. Run 'python sstreaming.py'
13. The data will be streamed to the folder C:/CC/TwiitterWikidata/twitter/streamtwitter/tweets/. 
    * An example of the initial file and overflow file has been added as a sample within the tweets folder of this project. 
    * If an error occurs streaming the data the data will auto start again starting with the file 'myprefix."current_date_time".json' and the overflow file 'streamer.""current_date_time".json'



# Part 2 Twitter Data Parsing

Part 2 parses the twitter live streamed data from Part 1 above, storing the results within the project structure. This processing includes cleaning of the tweets by extracting the hashtags per tweet, removing non-ASCII characters, removing strings of less than minimum length, splitting the tweets in to words, removing stop words of language English and storing the results for additional processing. The strings are split in preparation for applying n-grams. N-grams (1 to 4) is applied to the data. For each of the 4 n-gram output the spaces are stripped from the string, the hashtag occurrences are counted and ordered by the most frequent for further processing.

1. wordsonly1.py    - FROM  'streamtwitter/tweets' folder   ->   TO 'tweetwords' folder 
   * Take the tweets files in '.json' format  and parses the tweet removing the hashtag, removing non-ASCII characters, validate the line contains at least 2 characters and placing the content in the 'tweetwords' folder with file format 'Words_Only."current_date_time".csv' for additional processing. If the number of words added to the file is greater than or equal to 5000, a new file is created or if the end of the .json file is reached.

2. tokenisetwitter2.py    -from tweetwords folder /  to tokenisedtweets2 folder
   * This process takes the hashtag full words from step 1, splits the word in to individual words based on the 'wordsegment' python implementation, converts the string to lower case, removes stop words using the python implementation 'stopwords' of the English language. The result length is validated greater than 2 and output to a new .csv file 'tokenise."current_date_time".csv' for further processing. 

3. tokenisetwitter3.py   - from tokenisedtweets2 / to  tokenisetweets3 =>  break up big ngrams
   * This implementation breaks up the long split hashtags. Each line is processed separately - Firstly the line from the .csv file is read, and the sentence length in words is determined where a space indicates a new word. 
     * If the sentence length is less than 5 (equal to 4 words) print the full text to the new .csv file for further processing.
     * If the sentence length is equal to 5 words split the string in to the first 3 words and the last 2 words and add both to the output file. Then take the first 2 words and last 3 words of the same entry and add them to the output file.
     * If the sentence length is equal to 6 words split the string in to the first 3 words and the last 3 words and add both to the output file. 
     * If the sentence length is equal to 7 words split the string in to the first 4 words and the last 3 words and add both to the output file. Then take the first 3 words and last 4 words of the same entry and add them to the output file.
     * If the sentence length is equal to 8 words split the string in to the first 4 words and the last 4 words and add both to the output file

4. Apply n-grams (1-grams, 2-grams, 3-grams, 4-grams)
   * tokeniseengrams1.py - from tokenisetweets3 => to ngrams1 folder  => If the sentence length is equal 1 word add the word to the output file otherwise apply 1-grams to the text and output each word to the output file
   * tokeniseengrams2.py  - from tokenisetweets3 => to ngrams2 folder => If the sentence length is less than or equal to 2 word add the word to the output file otherwise apply 2-grams to the text and output each sentence to the output file.
   * tokeniseengrams3.py  - from tokenisetweets3 => to ngrams3 folder => If the sentence length is less than or equal to 3 word add the word to the output file otherwise apply 3-grams to the text and output each sentence to the output file.
   * tokeniseengrams4.py  - from tokenisetweets3   => to ngrams3 folder => Additional processing not required as 4 ngrams in tokenisetweets3 output file of previous step - execution of tokeniseengrams4.py results in no additional data as the large hashtags were already split in the previous step



5.  Remove spacing from the each of the n-gram output from step 4 before counting occurrences in each of the n-grams
    * Nothing to do for one words ones 1ngrams  # no change as there is no spaces in these words. 
    * removespacesgrams2.py     FROM ngrams2 folder  TO nspacesngram2                    
    * removespacesngrams3.py     FROM ngrams3 folder  TO nspacesngram3
    * removespacesngrams4.py     FROM tokenisedtweets3 folder  TO nspacesngram4


6. count words only - Count the number of occurrences of each hashtag word to output files (countwordsonly1.py initial test run file)
   * countwordsonlyngrams1.py     FROM ngrams1 folder  TO ngramscount1 
   * countwordsonlyngrams2.py     FROM nspacesngram2 folder  TO ngramscount2
   * countwordsonlyngrams3.py     FROM nspacesngram3 folder  TO ngramscount3
   * countwordsonlyngrams4.py     FROM nspacesngram4 folder  TO ngramscount4


7. get max words -  Orders the twitter results per n-gram folder based on those that occur most frequent (getmaxwords1.py initial test run file)
   * getmaxwordsngrams1.py   FROM ngramscount1 folder  TO orderedresultsngram1
   * getmaxwordsngrams2.py   FROM ngramscount2 folder  TO orderedresultsngram2
   * getmaxwordsngrams3.py   FROM ngramscount3 folder  TO orderedresultsngram3
   * getmaxwordsngrams4.py   FROM ngramscount4 folder  TO orderedresultsngram4



# Part 3 Wikidata XML Revision Parsing

1. Download python latest version for windows from here https://www.python.org/downloads/  for example click the yellow button 3.7.3
2. When installing select the checkbox to add to path
3. Select the custom option and then select the location item and add to c:python as the location (navigate to the location but create the folder python in the c:/ directory first)
4. Download pip by running the following from a dos prompt 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
5. Once finished run the following from the same command prompt 'python get-pip.py'
6. Navigate your DOS prompt to C:/python/scripts and run 'pip install SPARQLWrapper'
   

7. Assume that visual studio code https://visualstudio.microsoft.com/vs/ has already been installed and the project code has already been cloned and as outlined in Part 1 above.


8. Open a DOS prompt within visual studio code and navigate to C:\CC\TwiitterWikidata\twitter\streamtwitter
9.  The project python file 'parsexml.py' exists on the project and this will parse the wikidata xml file containing the revision data
10. The parsed data is added to a new additional folder here 'data'
11. Go to this site https://dumps.wikimedia.org/wikidatawiki/"wikidata dump date"/  (the selected date to download the wikidata dumps containing the wikidata metadata revision files)
    * Download each wikidata dump xml files for parsing for example wikidatawiki-20190601-stub-meta-history1.xml.gz
    * Select each one and unzip to a location - u will get an xml file  E.G. c:/wikidata/
    * Now start visual studio code from your start menu
    * On the console you will see add folder - navigate to C:\CC\TwiitterWikidata 
12. Ready to run the code
13. To run the code select 'terminal - new terminal' on the top menus in visual studio code- this will open a cmd terminal at the bottom of the page
14. Navigate to the location C:\CC\TwiitterWikidata\wikidata\parsewikidata 
15. Enter the command  'python parsexml.py' and run it.
16. You will see number output on the command prompt. This is a print out statement within the code showing the count of the number of revision items processed and can be comment out if not required within the code but validates the xml file is being processed successfully.
17. Additionally the output for the processed data can be seen in the output within the data folder .csv file that with 1 row per processed revision.  The data output is in the format "'pageid', 'pagetitle',  'label', 'revisionid', 'timestamp', 'comment', 'parentid'"



# Part 4 Wikidata processing

Having completed Part 3 of the process above where data is added to 'data' folder
* parsexml10.py         FROM  data  TO    wikidatalabels
  * firstly the wikidata titles are processed. The third element 'label' is extracted from the row item. Next the non-ASCII characters are removed and stop words of English language within the titles are also removed. The spaces between words is then removed and the content is added to a file .csv for additional processing.

* countwikidatawordsonly1.py     FROM wikidatalabels   TO orderedwikidataresults
  * Count the number of occurrences of each wikidata title where each count represents a revision to the page title. The value and total count is output to a file for further processing.

* getmaxwordswikidata1.py   FROM orderedwikidataresults  TO wikidataprocessed  
  * Orders the top wikidata revision titles by the mos frequently edited revision articles. The value and total per page item is output to a file for additional processing


# Part 5 Twitter and Wikidata analysis


1. Calculate Jaccard's Distance, Jaccard's Similarity, Kolmogorov-Smirnov statistic value and Kolmogorov-Smirnov p-value

* Initial Execution
  * Retrieve the list of wikidata items returned from Step 4 within the folder wikidataprocessed. The initial list had to be reduced in size because of out of memory exception errors that resulted when running the statistical formula - File 'SimplifiedList.csv'. All wikidata items with a total revisions of greater than three were added to a new list .csv file for use when calculating the statistical measures

  * The file statistics.py contains the statistical formula for calculating Jaccards Distance, Jaccards Similarity, kolmogorov-smirnov statistic value and kolmogorov-smirnov p-value 
    * **Each formula is run per n-grams (1-gram, 2-gram, 3-gram, 4-gram)**
    * **This statistical formula processing run for 100%, 50%, 10% and .1% of both the twitter data and wikidata across each of the n-grams (1-gram, 2-gram, 3-gram, 4-gram)>**
    * **The implementation for each is contained within the folder graphs and its sub folders 100, 50, 10, 1 with each of the formula above executed for each set of data**
    * Note - depending on processing when all the statistical formula are run as one file memory errors may be occur. If this occurs run each statistical formula individually by commenting out the remaining statistical calculation. Run each calculation in turn individually.


2. Graphs / Charts  

* This class takes the data output from wikidata processed in Part 4 'wikidataprocessed' and splits the data in to 2 fields 'name' and 'total', the results in then placed in graphs/wikidatafinal.csv file
* This is run by execution of the command 'python splitdatatofields.py'



**Charts**
* One list for wikidata (always same  one taken from )), one list for twitter per ngram list from files. The process 'python splitdatatofields.py' splitting the fields in to 'name' and total is applied to the files within the orderedresultsngram1, orderedresultsngram2, orderedresultsngram3, orderedresultsngram4 and the content copied to a new file as follows. The copying of this data to the new file is a manual process. This removed any brackets and quotes and places the content in individual rows and fields where the fields are separated by a comma in the .csv file.
  * ngramschartsONE.py (copy of the content in count.csv orderedresultsngram1 split in to 2 columns)
  * ngramschartsTWO.py (opy of the content in count.csv orderedresultsngram4 split in to 2 columns)
  * ngramschartsTHREE.py (dopy of the content in count.csv orderedresultsngram3 split in to 2 columns)
  * ngramsChartsFour.py (copy of the content in  count.csv  orderedresultsngram4 split in to 2 columns)

* BarChartNGrams1Hashtags.py (Uses ngramschartsONE.csv)
  * Top Twenty Most Frequent Twitter Hashtags with 1-Grams' +'\n' + '15th March 2019 to 1st June 2019
* BarChartNGrams2Hashtags.py (Uses ngramschartsTWO.csv)
  * Top Twenty Most Frequent Twitter Hashtags with 2-Grams' +'\n' + '15th March 2019 to 1st June 2019
* BarChartNGrams3Hashtags.py (Uses ngramschartsTHREE.csv)
  * Top Twenty Most Frequent Twitter Hashtags with 3-Grams' +'\n' + '15th March 2019 to 1st June 2019
* BarChartNGrams4Hashtags.py (Uses ngramschartsFOUR.csv)
  * Top Twenty Most Frequent Twitter Hashtags with 4-Grams' +'\n' + '15th March 2019 to 1st June 2019
* BarChartSummaryTotalsTwitter.py 
  * Total Twitter Hashtags Processed Per N-Grams
* BarChartSummaryTotalsWikidata.py 
  * Total Unique Wikidata Pages (Collected and Processed)
  * Total Wikidata Pages and and Revisions '  +'\n' + '15th March 2019 to 1st June 2019
* BarChartWikidataRevisions.py (Uses wikidatafinal.csv.csv)
  * Top Twenty Most Frequent Wikidata Revisions ' +'\n' + '15th March 2019 to 1st June 2019
* Word cloud charts were completed in RStudio using the language R. 







