import os
import tweepy

# Load dari environment
consumer_key = os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_SECRET_KEY')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Validasi
for key, val in {
    "TWITTER_API_KEY": consumer_key,
    "TWITTER_API_SECRET_KEY": consumer_secret,
    "TWITTER_ACCESS_TOKEN": access_token,
    "TWITTER_ACCESS_TOKEN_SECRET": access_token_secret
}.items():
    if val is None:
        raise RuntimeError(f"Missing env variable: {key}")

# Autentikasi OAuth1 (v1.1)
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

# Teks tweet
tweet_text = "Halo!"

# Posting
response = api.update_status(status=tweet_text)
print("Tweet posted successfully:", response.id)
