# This class live streams the data from twitter https://www.tweepy.org/
from tweepy import StreamListener
import json, time, sys

class SListener(StreamListener):

    # Initiate the streamer process starting the counter at 0. the file is created starting 
    # with the word streamer followed by the current date time that is of file type json and 
    # is a writable file.
    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api
        self.counter = 0
        self.fprefix = fprefix
        self.output  = open(fprefix + '.'  + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        self.delout  = open('deletefile.txt', 'a')

    # Function to handle the data where if data the on_status method is called to write the data
    # to the output file up to a total number of 500. This method also handles the errors like limit 
    # reached and warnings. In these cases the details are output and the process is continued.
    def on_data(self, data):
        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print(warning['message'])
            return False

    def on_status(self, status):
        self.output.write(status + "\n")
        self.counter += 1
        # If the number of tweets output is 500 create a new file with the name 'streamer' 
        # concatinating the data time of creation ending with the extension .json that is 
        # a writable to file. Reset the counter back to 0 to begin counting for the new file.
        if self.counter == 500:
            self.output.close()
            self.output  = open('streamer' + '.' + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
            self.counter = 0
        return
        
    def on_delete(self, status_id, user_id):
        self.delout.write( str(status_id) + "\n")
        return

    # Function to output limit error that may occur outputting details to the console.
    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    # Function to handle error method writing out the error code to the console.
    def on_error(self, status_code):
        sys.stderr.write('Error Occurred: ' + str(status_code) + "\n")
        return False

    # Function to handle a time out with a sleep for 1 minute built in where 
    # processing will then continue.
    def on_timeout(self):
        sys.stderr.write("Timeout occurred, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 