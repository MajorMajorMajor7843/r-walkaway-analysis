import matplotlib.pyplot as plt
import numpy as np
import pylab

import praw
reddit = praw.Reddit(INFO)

subreddit = reddit.subreddit('lotrmemes')

popular = subreddit.hot(limit = 1000)

users = []

for posts in popular:
    try:
        users.append(posts.author.name)
    except Exception:
        print ("something wrong with " + posts.title)
    posts.comments.replace_more(limit = 0)
    for comment in posts.comments.list():
            try:
                users.append(comment.author.name)
            except:
                print ("something wrong with " + comment.body)
                pass


users = list(set(users))
if "TotesMessenger" in users:
    users.remove("TotesMessenger")

if "imguralbumbot" in users:
    users.remove("imguralbumbot")

if "election_info_bot" in users:
    users.remove("elecetion_info_bot")


for user in users:
    karma_PM = 0
    karma_LM = 0
    try:
        for comment in reddit.redditor(user).comments.new(limit=500):
            if (comment.subreddit == "lotrmemes"):
                karma_LM += comment.score
            if (comment.subreddit == "PrequelMemes"):
                karma_PM += comment.score
                
        karma_dict[user] = (karma_LM,karma_PM)
    except Exception:
        print ("something wrong with " + user)
        pass

#print (karma_dict)


histogram = []
more_than_thousand = []

both_user = []

num_user = 0
for key in karma_dict:
    karma = karma_dict[key]
    if (karma[0] > 10 and karma[1] > 10):
        num_user += 1
        both_user.append(key)
    histogram.append(karma[1])
    if (karma[1] > 1000 and karma[0] > 10):
        more_than_thousand.append(key)
        
    
    
 
print (both_user)
   

print ("The length of the dictionary is " + str(len(karma_dict)))

print ("People using both prequel meme and lotrmeme is " + str(num_user))

print (more_than_thousand)


plt.figure(figsize=(10,12))

plt.hist(histogram, bins = 50)
plt.ylabel('Number of occurence of karma points')
plt.xlabel('Comment karma in r/PrequelMeme')
plt.title('Distribution of karma in r/PrequelMeme among r/lotrmemes users')

plt.figure(figsize = (100,100))

pylab.savefig('lotrmeme.png')
