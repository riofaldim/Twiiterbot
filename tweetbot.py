import os
import tweepy
import time

# Load environment variables
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Verify credentials
try:
    api.verify_credentials()
    print("Authentication OK")
except tweepy.TweepyException as e:
    print(f"Error during authentication: {e}")
    exit()

# Helper functions for tracking last seen tweet ID
SEEN_FILE = 'seen.txt'

def read_seen(file):
    try:
        with open(file, 'r') as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 1  # Return a default minimum tweet ID if file doesn't exist

def store_seen(file, last_seen_id):
    with open(file, 'w') as f:
        f.write(str(last_seen_id))

# Main reply function
def reply():
    last_seen_id = read_seen(SEEN_FILE)
    try:
        tweets = api.mentions_timeline(since_id=last_seen_id, tweet_mode='extended')
        for tweet in reversed(tweets):
            if '#hello' in tweet.full_text.lower():
                username = tweet.user.screen_name
                print(f"Replying to @{username} (ID: {tweet.id})")
                try:
                    api.update_status(
                        status=f"@{username} All the best!",
                        in_reply_to_status_id=tweet.id
                    )
                    api.create_favorite(tweet.id)
                    api.retweet(tweet.id)
                except tweepy.TweepyException as e:
                    print(f"Error replying to tweet: {e}")
                store_seen(SEEN_FILE, tweet.id)
    except tweepy.TweepyException as e:
        print(f"Error fetching mentions: {e}")

# Loop execution
if __name__ == "__main__":
    while True:
        reply()
        print("Checked mentions... Waiting...")
        time.sleep(15)
