# TwiitterWikidata
Project identifying if a correlation exists between live streamed Twitter hashtags and Wikidata revisions.

###################################################
#
#Part 1 Twitter Data Live Streaming  
#
####################################################
#https://www.tweepy.org/
1. Install visual studio code
2. Run 'pip install tweepy' to install tweepy that required to stream live twitter data
3. Go to http://apps.twitter.com and create an app.
4. The consumer keys and tokens are found within the application details page located located at https://dev.twitter.com/apps (found within the "OAuth settings")
5. Add the account specific details for consumer key and secret within the file ssstreaming.py replacing the ****** value key and token with those obtained from twitter app.
         #consumer_key="***************************"
         #consumer_secret="*****************************************"

6. After the step above, you will be redirected to your app's page.
7. Create an access token under the the "Your access token" section.  The access tokens located in the application details page located at  https://dev.twitter.com/apps (found within the "Your access token") 
8. Add access token and secret specific tokens within the file sstreaming.py replacing the ***** value token and secret with those obtained from the twitter app.
         #access_token="*****************************************"
         #access_token_secret="****************************************"
9. Navigate to C:\CC\TwiitterWikidata\twitter\streamtwitter
10. Run 'python sstreaming.py
11. The data will be streamed to the folder wikidataout. An example of the initial file and overflow file has been added as a sample within the wikidataout folder of this project. If an error occurs streaming the data the data will auto start again starrting with the file 'myprefix.<date-time>.json' and the overflow file 'streamer.<date-time>.json'


###################################################
#
#Part 2 Twitter data parsing
#
###################################################


Part 3 Wikidata xml revision parsing
1. Download python latest version for windows from here https://www.python.org/downloads/  for example click the yellow button 3.7.3
2. When installing select the checkbox to add to path
3. Select the custom option and then select the location item and add to c:python as the location (navigate to the location but create the folder python in c:/ first)

4. Download pip by running the following from a dos prompt 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
6. Once finished run the following from the same command prompt 'python get-pip.py'

7. Navigate your dos prompt to C:/python/scripts and run 'pip install SPARQLWrapper'
8. Download visual studio code https://visualstudio.microsoft.com/vs/

9. Create a new project folder on your cdrive   C:\CC\TwiitterWikidata and add the subfolders '\wikidata\parsewikidata'
10. The project python file 'parsexml.py' is added to the project and this will parse the wikidata xml file containing the revision data
11. The parsed data is added to a new additional folder here 'wikidataout'
12. Go to this site https://dumps.wikimedia.org/wikidatawiki/<wikidata dump date>/  (the selected date to download the wikidata dumps containing the wikidata metadata revision files)
        Download each wikidata dump xml files for parsing for example wikidatawiki-20190601-stub-meta-history1.xml.gz  
        Select each one and unzip to a location - u will get an xml file  E.G. c:/wikidata/
        Now start visual studio code from your start menu
        On the console you will see add folder - navigate to C:\CC\TwiitterWikidata and open

13. Ready to run the code
14. To run the code select 'terminal - new terminal' on the top menus in visual studio code- this will open a cmd terminal at the bottom of the page
15. Navigate to the locsstion location C:\CC\TwiitterWikidata\wikidata\parsewikidata 
16. Enter the command  'python parsexml.py' and run it.
16. You will see number output on the command prompt. This is a print out statement within the code showing the count of the number of revision items processed and can be comment out if not required within the code but validates the xml file is being processed successfully.
17. Additionlly the output for the processed data can be seen in the output .csv file that with 1 row per processed revision located in.  The data output is in the format "'pageid', 'pagetitle',  'label', 'revisionid', 'timestamp', 'comment', 'parentid'"






###################################################
#
#Part 4 Wikidata processing
#
###################################################





###################################################
#
#Part 5 Twitter and Wikidata analysis
#
###################################################


