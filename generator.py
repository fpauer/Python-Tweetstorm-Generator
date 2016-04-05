class Generator(object):
   """ 
     This class create a tweeter strom from a file:

	Example for use:
	
	
        $ python example.py

	# example.py
		from generator import Generator
		g = Generator('tweet.txt')
		tweetList = g.tweetStorm()
		total = len(tweetList)
		for idx, tweet in enumerate(tweetList, start=1):
		    print "%d/%d %s" % (idx,total,tweet)

     This class should be modified in the future to accept 
     string variables, JSON data, etc as input 

   """
   
   minEdge = 0
   maxEdge = 0
   tweetSize = 140 
   tweetList = []
   filename = None 
   data = None

   def __init__(self, filename):
	""" 
	     Constructor to read a file and divide the content in tweets with 140 characters
        """
	self.filename = filename
   	self.minEdge = (self.tweetSize*0.85)
   	self.maxEdge = (self.tweetSize*0.98)
	

   def tweetStorm(self):
	""" 
	     The main method resposable to open the file read and create the tweets
        """
	with open(self.filename, 'r') as textfile:
    		self.data=textfile.read().replace('\n', '')
	
	self.divideTweet(self.data, self.tweetSize)
        return self.tweetList

   def divideTweet(self, text, n):
	""" 
	     This method divide a string/text into small piece of texts 
             with 140 characters each one
        """

	# if the text has les than 140 so return
	if len(text) <= n :
		self.tweetList.append(text)
		return

	while len(text) > n :

		end = n
		subtext = text[0:end]
		lastPos = subtext.rfind('.')
	
		# if exist a point almost at the end and create a better phrase to conclude the meaning
		if lastPos >= self.minEdge and lastPos <= self.maxEdge:
			end = lastPos
		else:
			# if exist a comma almost at the end and create a better phrase to conclude the meaning
			lastPos = subtext.rfind(',')
			if lastPos >= self.minEdge and lastPos <= self.maxEdge:
				end = lastPos
			# get the last space between words to divide better the text
			else: end = subtext.rfind(' ')
	
		subtext = text[0:end+1]

		# append the subtext to the result list
		self.tweetList.append(subtext)

		# remove from the original text the previous subtext 
		text = text[end+1:len(text)]

	subtext = text[0:len(text)]
        self.tweetList.append(subtext)

