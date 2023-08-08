import tweepy

# Set up the Twitter API credentials
API_KEY = ""
API_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Authenticate to the API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

positive_words = ["good", "great", "excellent", "efficient", "love", "like", "enjoy", "favorable", "commendable", "superb"]
queries = [f"public transport {word}" for word in positive_words]

num_of_tweets_per_query = 10  

for query in queries:
    print(f"Fetching tweets for query: {query}")
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(num_of_tweets_per_query)
    
    for tweet in tweets:
        print(tweet.text)
        print("-----------------------")
