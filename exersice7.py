import tweepy

consumer_key = 'ygtPMjctL62Pg20icSwl6VNxU'
consumer_secret = 'WASx6GxZbsLEs064THx68GucFVYVo5cqsloW5ngvzP3K2L2XgC'
access_token = '1730249119-7E4iT1XKqVBpgeJScVPuMTSCl52Jot1uoqbUjkH'
access_token_secret = 'NhCmLUDnBwVD7mWGpnWnXlHijwF73Dctcj0cQUbC3PYtY'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)
 
def get_all_tweets(screen_name):
		
	alltweets = []	
	new_tweets = api.user_timeline(screen_name = screen_name, count = 10)	
	alltweets.extend(new_tweets)
	tLen = 0

	for tweet in alltweets:
		tLen = tLen + len(tweet.text)
		
	return tLen


username1 = raw_input('Enter Twitter User 1: ')
username2 = raw_input('Enter Twitter User 2: ')

counter1 = get_all_tweets(username1)
counter2 = get_all_tweets(username2)

if counter1>counter2:
	print ("User " + username1 + " has : " + str(counter1))
	print ("User " + username1 + " has used more words in his last 10 tweets than " + username2)
else:
	print ("User " + username2 + " has : " + str(counter2))
	print ("User " + username2 + " has used more words in his last 10 tweets than " + username1)
