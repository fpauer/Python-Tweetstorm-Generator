from generator import Generator

g = Generator('tweet_large.txt')
tweetList = g.tweetStorm()
total = len(tweetList)
for idx, tweet in enumerate(tweetList, start=1):
    print "%d/%d %s" % (idx,total,tweet)

