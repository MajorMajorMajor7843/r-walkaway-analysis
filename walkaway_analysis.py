import matplotlib.pyplot as plt
import numpy as np
import pylab

import praw
reddit = praw.Reddit(STUFF)

subreddit = reddit.subreddit('Walkaway')

popular = subreddit.hot(limit = 200)

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

##print (users)
#
#
#print (users[0])
#karma = 0
#
#for comment in reddit.redditor(users[0]).comments.new(limit=None):
#    if (comment.subreddit == "The_Donald"):
#        print (comment.body)
#        print (comment.score)
#        karma += comment.score
#
#print (karma)
#
karma_dict = {}


for user in users:
    karma_TD = 0
    karma_WA = 0
    try:
        for comment in reddit.redditor(user).comments.new(limit=500):
            if (comment.subreddit == "The_Donald"):
                karma_TD += comment.score
            if (comment.subreddit == "Walkaway"):
                karma_WA += comment.score
                
        karma_dict[user] = (karma_TD,karma_WA)
    except Exception:
        print ("something wrong with " + user)

print (karma_dict)


histogram = []
more_than_thousand = []

num_fake = 0
for key in karma_dict:
    karma = karma_dict[key]
    if (karma[0] > 25 and karma[1] > 10):
        num_fake += 1
    if (karma[1] > 10):
        histogram.append(karma[0])
    if (karma[0] > 1000):
        more_than_thousand.append(key)
        
    
    
        
   

print ("The length of the dictionary is " + str(len(karma_dict)))

print ("Fake people are " + str(num_fake))

print (more_than_thousand)


plt.figure(figsize=(10,12))

plt.hist(histogram, bins = 50)
plt.ylabel('Number of occurence of karma points')
plt.xlabel('Comment karma in r/The_Donald')
plt.title('Distribution of karma in r/The_Donald')

pylab.savefig('walkaway.png')
