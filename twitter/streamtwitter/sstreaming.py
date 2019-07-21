# This class defines the twitter tokens and keys required to 
# stream twitter data https://www.tweepy.org/
from slistener import SListener
import time, tweepy, sys

# Go to http://apps.twitter.com and create an app.
# The consumer keys and tokens are found within the application details
# page located located at https://dev.twitter.com/apps (found within the 
# "OAuth settings")
# Add the account specific details here for consumer key and secret
#consumer_key="***************************"
#consumer_secret="*****************************************"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section.
# The access tokens located in the application details page located at 
# https://dev.twitter.com/apps (found within the "Your access token")
# Add access token and secret specific tokens
#access_token="*****************************************"
#access_token_secret="****************************************"
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# tweepy API call with authentication details
api = tweepy.API(auth)

# Main method function to live stream the twitter data with any 
# tweet containing '#' that is of language English 'en'
def main():
    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)
    print("Streaming started...")

    # Filter the tweets by those containing a hashtag '#' that are of
    # language English 'en'.
    try: 
        stream.filter(track = '#', languages=['en'])
    except:
        # If an exception occurs catch the acception, disconnect the stream
        # and start the streaming process again.
        print("error!")
        print("continuing again ......!")
        stream.disconnect()
        print("Start Again ......!")
        main()

# Start the streaming process.
if __name__ == '__main__': 
    main()