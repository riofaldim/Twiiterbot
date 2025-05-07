# 📌 Twitter Bot with Tweepy

A Twitter bot that listens for mentions with the hashtag #hello and replies with "All the best" while also liking and retweeting the tweet

## 🚀 Overview

This project utilizes Tweepy to interact with the Twitter API. The bot continuously checks for new mentions and automatically responds, likes, and retweets tweets containing a specific hashtag.

## 🛠 Features

✅ Monitors mentions in real-time
✅ Replies to tweets containing #hello
✅ Likes and retweets mentioned tweets
✅ Stores processed tweet IDs to avoid duplicate replies

## 🏗 Tech Stack

- Programming Language: Python
- Libraries: Tweepy, OS, Time
= APIs: Twitter API

## 🎬 Installation & Usage

### Prerequisites
1. Twitter Developer Account - You need API keys from Twitter.
2. Python 3.x installed on your system.

### Installation
1.Clone the repository:
```
git clone https://github.com/yourusername/tweetbot.git
cd tweetbot
```
2.Install dependencies:
```
pip install -r requirements.txt
```
3.Set up environment variables (.env file):
```
CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
ACCESS_KEY=your_access_key
ACCESS_SECRET=your_access_secret
```
4.Run the bot:
```
python tweetbot.py
```
## 📂 Project Structure
📦 tweetbot
 ┣ 📜 tweetbot.py         # Main script
 ┣ 📜 seen.txt            # Stores last processed tweet ID
 ┣ 📜 .env                # Environment variables
 ┣ 📜 README.md           # Project documentation
 ┣ 📜 requirements.txt    # Dependencies
 ┣ 📜 .gitignore          # Ignore unnecessary files
 
## 📜 License
This project is licensed under the MIT License. 

**Ease your tweeting with tweetbot**
