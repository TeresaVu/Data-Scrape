from TikTokApi import TikTokApi
import pandas as pd

api = TikTokApi()

tiktokUrls = ["https://www.tiktok.com/@tiktoktips/video/7068819016588037418?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/7068816944459304234?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/7068815322320571691?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/7068814232896277806?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/7068812229059267886?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/6854304331622010118?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/6854302292800179461?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/6854300350510402822?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/6854297925187685638?is_copy_url=1&is_from_webapp=v1&lang=en",\
"https://www.tiktok.com/@tiktoktips/video/6854295790249151750?is_copy_url=1&is_from_webapp=v1&lang=en"]

comments = []
numComments = 30
# get the tiktok specified by each url and get its comments
for tiktok in tiktokUrls:
    video = api.video(url=tiktok)
    print(video.stats)
    comments.append([tiktok[0], video.create_time, video.author.username, video.stats['commentCount'], video.stats['diggCount'], video.stats['playCount'], video.stats['shareCount']])
    # each row in the dataframe will contain this content
    # for comment in api.video(url=tiktok).comments(numComments):
    #     comments.append(['-', '-', comment.author.username, comment.text, comment.likes_count, '-', '-'])
    
    # testing
    while True:
        try:
            for comment in reversed(video.comments(numComments)):
                pass
            print(f"Comment count excluding replies: {numComments}")
            break
        except:
            numComments -= 1
            continue
    break

# Creating a dataframe from the comments list above 
commentsDF = pd.DataFrame(comments, columns=["URL", "Date", "Username", "Comments", "Number of Likes", "Number of Views", "Number of Shares"])
print(commentsDF)