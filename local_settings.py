'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = '96abVWe1qZjIwsDfPHQvNdo32'
MY_CONSUMER_SECRET = 'MxoFmdip45VIEFQIsocnBTiknBIDipqQQwxCFmKq5bL69NFY3w'
MY_ACCESS_TOKEN_KEY = '2517830347-InlkvZPbD4COOFcdNXDKp6VnplA42KMcc9mHvj0'
MY_ACCESS_TOKEN_SECRET = 'VP6IUGb7Mw6I1OCOeVv2MbeRdrIZOCbuETG8Q3cWoSqeV'

SOURCE_ACCOUNTS = ["https://twitter.com/Dan_Rowinski"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "https://twitter.com/Rowinski_Ebooks" #The name of the account you're tweeting to.
