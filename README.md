# headphone-bot
This is a pretty simple app to monitor /r/buildapcsales on reddit for headphone deals using PRAW and Twilio. However, it can be used to look for pretty much any type of deal on any subreddit. 

## Use
To use, make sure you run <code>pip -r requirements.txt</code> and set the following environment variables for Twilio:
* TWILIO\_ACCOUNT\_SID -- your account sid from Twilio
* TWILIO\_AUTH\_TOKEN  -- your auth token from Twilio
* TWILIO\_NUMBER       -- your phone number from Twilio
* TO\_PHONE\_NUMBER    -- the phone number you are sending things to

Also set the following for the reddit interface (this one might take some setting up, due to Reddit's Terms of Service you will need to register your bot with them. The full instructions are on the PRAW docs.):
* REDDIT\_CLIENT\_ID     -- your client id for the bot
* REDDIT\_CLIENT\_SECRET -- your client secret for the bot
* REDDIT\_USER\_AGENT    -- your user agent for the bot

Then simply run <code>python headphone_sale_bot.py</code>

To update the tags, simply add them to the <code>deal_tags</code> variable, and to adjust the subreddit to search adjust the <code>streaming_subreddit</code> varaible. Later this will be turned into a CLI, but for my purposes this works.
