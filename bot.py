BOT_USERNAME      = 'BOT_USERNAME'
BOT_PASSWORD      = 'BOT_PASSWORD'
BOT_CLIENT_ID     = 'BOT_CLIENT_ID'
BOT_CLIENT_SECRET = 'BOT_CLIENT_SECRET'
BOT_USER_AGENT    = 'BOT_USER_AGENT'

TARGET_SUBREDDIT  = 'test'
REPLY_CONTENT     = 'Please set a user flair.'

#replace above with your own

import praw
from os import path
import time


LOG_FILE_PATH = './all_replied_comments_log.txt' #you can change this if you want



logs = []

if path.exists(LOG_FILE_PATH):
    file = open(LOG_FILE_PATH)
    logs = file.read().split('\n')
    file.close()



class FlairBot:
    def __init__(self):
        self.reddit = praw.Reddit(username=BOT_USERNAME,
                         password=BOT_PASSWORD,
                         client_id=BOT_CLIENT_ID,
                         client_secret=BOT_CLIENT_SECRET,
                         user_agent=BOT_USER_AGENT)

    def record_logs(self):
        log_file = open(LOG_FILE_PATH,'w')
        log_file.write('\n'.join(logs))
        log_file.close()
        
    def run(self):
        
        for comment in self.reddit.subreddit(TARGET_SUBREDDIT).comments(limit=1000):
            
            if comment.id not in logs and comment.author != reddit.user.me() and comment.author_flair_text==None:
                comment.reply(REPLY_CONTENT)
                log.append(comment.id)
                            
            print('Replied to user: '+comment.author+'.')

        self.record_logs()
        
if __name__ == '__main__':
    bot = Bot()
    
    while True:
        try:
            print('Started!')
            bot.run()
            print('Completed! Sleeping for 10 seconds...')
            time.sleep(10)
        except Exception as e:
            print(e)


            
