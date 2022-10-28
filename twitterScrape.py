import snscrape.modules.twitter as sntwitter
import pandas as pd

# Created a list to append all tweet attributes(data)
mediaLitWeek = []
digCitWeek = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('#MediaLitWeek').get_items()):
    mediaLitWeek.append([tweet.date.date(), tweet.likeCount, tweet.user.username, tweet.content])

for i,tweet in enumerate(sntwitter.TwitterHashtagScraper('#DigCitWeek').get_items()):
    digCitWeek.append([tweet.date.date(), tweet.likeCount, tweet.user.username, tweet.content])
    
# Creating a dataframe from the tweets list above 
mediaDF = pd.DataFrame(mediaLitWeek, columns=["Date Created", "Like Count", "User", "Tweets"])
print(mediaDF)

digDF = pd.DataFrame(digCitWeek, columns=["Date Created", "Like Count", "User", "Tweets"])
print(digDF)

# export the dataframe to a csv file if desired
# mediaDF.to_csv("#MediaLitWeek.csv") 
# digDF.to_csv("#DigCitWeek")