import tweepy

API_P = "hGsNwUHfulv96hHMkiea5dXLc"
API_S = "Su3zxlOVVmo4JOYm5D7RJZmvDP5luuczKuWbZTWQZ9zHAxQ26Z"

Access_P = "852541877702275072-zOCzsHAqjMFXJpYpYkaHZq4xaeeXD2J"
Access_S= "TDTWjEfb9fP3C5x81GC5unOsVGLuLZPSFER817bkmE9U2"

auth = tweepy.OAuthHandler(API_P, API_S)
auth.set_access_token(Access_P, Access_S)
api = tweepy.API(auth)

def Tweet_timeline():
    user_search = input("What user do you want to check: ")
    user = api.user_timeline(user_search)
    for tweet in user:
        print(tweet.text)
