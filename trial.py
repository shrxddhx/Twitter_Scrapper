import twint
import datetime

# Configure Twint first
conf = twint.Config()

def twindler_search(name, text):
    # Account Name, for example "elonmusk", etc.
    conf.Username = name
    # Text of the Twitter
    conf.Search = text
    # Limit search results to 20 tweets
    conf.Limit = 20
    # Run
    twint.run.Search(conf)
    
if __name__ == "__main__":
    name=input("Enter a username you want to scrap tweets from: ")
    text=input("Enter a keyword you want in the tweets: ")
    twindler_search(name, text)
