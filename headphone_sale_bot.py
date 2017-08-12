# Just a quick bot to monitor the sales on r/buildapcsales
# 
# I'm in the market for a new headphone set and want to get texts when there is a sale

import os

import praw
import twilio.rest

deal_tags = ["headphones"]
streaming_subreddit = "buildapcsales"
to_phone_number = os.environ.get("TO_PHONE_NUMBER")
body_template = "New deal on buildapcsales! Here is the link to the deal: {}"

def load_twilio_config():
    twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_number = os.environ.get('TWILIO_NUMBER')

    if not all([twilio_number, twilio_account_sid, twilio_auth_token]):
        raise Exception("Twilio environment variables not configured")

    return (twilio_number, twilio_account_sid, twilio_auth_token)

def load_reddit_config():
    reddit_client_id = os.environ.get("REDDIT_CLIENT_ID")
    reddit_client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
    reddit_user_agent = os.environ.get("REDDIT_USER_AGENT")

    if not all([reddit_client_id, reddit_client_secret, reddit_user_agent]):
        raise Exception("Reddit environment variables not configured")

    return praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)

# based on the notification tutorial
class MessageClient(object):
    def __init__(self):
        (twilio_number, twilio_account_sid, twilio_auth_token) = load_twilio_config()

        self.twilio_number = twilio_number
        self.twilio_client = twilio.rest.Client(twilio_account_sid, twilio_auth_token)

    def send_message(self, body, to):
        self.twilio_client.messages.create(body=body, to=to, from_=self.twilio_number)

# main loop that will grab the newest posts from r/buildapcsales and see if the tags match 
# anything I want to be notified about
def main():
    messager = MessageClient()
    reddit = load_reddit_config()

    for submission in reddit.subreddit(streaming_subreddit).stream.submissions():
        if any([("[{}]".format(x) in submission.title.lower()) for x in deal_tags]):
            print("Found deal! {}".format(submission.shortlink))
            messager.send_message(to=to_phone_number, body=body_template.format(submission.shortlink))


if __name__ == "__main__":
    main()
