import tweepy
import os

# Load credentials from environment variables
consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

# Tweet content
tweet_text = "Jasa Lacak Lokasi Akurat ✅"
image_path = "1743945574066.jpg"

# Upload media and tweet
media = api.media_upload(image_path)
api.update_status(status=tweet_text, media_ids=[media.media_id])

print("Tweet berhasil dikirim.")
