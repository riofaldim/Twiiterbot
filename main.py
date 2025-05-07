import os
import tweepy
import json
import requests

# Load Twitter API credentials from environment
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Load quotes from JSON file
with open('quotes.json', 'r') as f:
    quotes = json.load(f)

# Load last tweeted quote index from file, default to -1 if not found
index_file = 'last_tweet_index.txt'
if os.path.exists(index_file):
    with open(index_file, 'r') as f:
        try:
            tweet_index = int(f.read().strip())
        except ValueError:
            tweet_index = -1
else:
    tweet_index = -1

# Calculate next index
tweet_index = (tweet_index + 1) % len(quotes)
quote = quotes[tweet_index]
tweet_text = f'"{quote["quote"]}" - {quote["character"]}'

# Optional: Tweet with image
# image_url = quote.get('image')
# if image_url:
#     image_data = requests.get(image_url).content
#     with open("temp.jpg", "wb") as img_file:
#         img_file.write(image_data)

#     client = tweepy.Client(
#         consumer_key=consumer_key,
#         consumer_secret=consumer_secret,
#         access_token=access_token,
#         access_token_secret=access_token_secret
#     )
#     media = client.media_upload("temp.jpg")
#     response = client.create_tweet(text=tweet_text, media_ids=[media.media_id])
# else:

# Authenticate and tweet
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

response = client.create_tweet(text=tweet_text)
print(f'Tweeted: {tweet_text}')

# Save next index
with open(index_file, 'w') as f:
    f.write(str(tweet_index))
