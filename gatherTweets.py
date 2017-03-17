#Conner Leverett 

# Import the necessary package to process data in JSON format
try:
	import json
except ImportError:
	import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import time
import datetime 


####This code was found here: http://geospatialpython.com/2011/01/point-in-polygon.html and was not written by Conner Leverett
def point_in_poly(x,y,poly):
# Determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs. This function
# returns True or False.  The algorithm is called
# the "Ray Casting Method".
	n = len(poly)
	inside = False

	p1x,p1y = poly[0]
	for i in range(n+1):
		p2x,p2y = poly[i % n]
		if y > min(p1y,p2y):
			if y <= max(p1y,p2y):
				if x <= max(p1x,p2x):
					if p1y != p2y:
						xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
					if p1x == p2x or x <= xints:
						inside = not inside
		p1x,p1y = p2x,p2y
	return inside

outlineOfStates=[[-123.2899461863574,35.67137503893398],[ -119.8174278565946,33.03696150203579],[-116.1930012478764,31.65236673017377],\
[-112.4003495143584,30.55915816579148], [-112.0865595176321,30.49100199554992],[-107.385279449725,30.43583870490074],\
[-103.9144497612053,27.61755430985981],[-103.7692925035189,27.56669017611785],[-99.86903280745864,25.86632937378808],\
[-96.75725149229236,25.92657686445639],[-95.71894103158193,28.22292989385912],[-92.182397830726,28.79015852166426],\
[-85.90456199296085,27.65923485189989],[-82.82963706122817,24.87841175573972],[-79.28286270747447,24.34198843332917],\
[-77.55782652404042,28.23492205354584],[-75.39433505192631,34.58956677180203],[-71.75060370092898,39.78563047722661],\
[-68.14396542788511,42.32292057448612],[-66.02168633981911,45.00336656097898],[-67.0935697690214,46.95176061090069],\
[-69.73434560627835,47.7265039114173], [-71.95840904568986,46.54591705356772], [-76.09495379308115,45.30213699338995],\
[-79.43682289424352,43.95226707844498], [-81.43259888406212,42.39614488131808], [-81.68555908015996,46.44649818596999],\
[-86.89113388420255,48.58399826242675], [-91.83397724751315,49.12163533442404], [-96.07903592185365,49.44930972969811],\
[-119.1929774290291,49.91670978296965], [-125.5048764836463,49.6857795881536],[-126.8046538159266,46.67653922600668],\
[-123.2899461863574,35.67137503893398]]

#The code used to access Twitter is taken from here: http://socialmedia-class.org/twittertutorial.html
consumer_key = 'pQCn49jJCMVk5v70zeamnGwei'
consumer_secret = 'fsGrkU11AFaxv4EGzPBK443tfrRDnij8gMAx1B6CtUxRz3FyMi'
access_token = '1159021298-O9XRY4CoGLfDeDpUveqaI2EAUIlMyc5yGKn66Nc'
access_secret = 'zqfwxqxRYi0ppwA1eIDZgLGUuAVnQWN1J2xTqvxOaEdMZ'

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

datetimeNow = datetime.datetime.now()

#This is just formatting
hour = "%02d" % (datetimeNow.hour,)
minutes = "%02d" % (datetimeNow.minute,)

dateForFileName = str(datetimeNow.year)+'-'+str(datetimeNow.month)+'-'+str(datetimeNow.day)+ ' ' + hour + minutes

fileToWriteTo = open('output '+dateForFileName+'.txt', 'w')

fileToWriteTo.write('TweetID,TweetText,Hashtags,Latitude,Longitude\n')


tweetidList = []


for z in range(5):
	print z
	tweet_count = 0
	for tweet in iterator:
		tweet_count = tweet_count+ 1	
		try:
			if tweet['geo']!=None:
				if (point_in_poly(tweet['geo']['coordinates'][1],tweet['geo']['coordinates'][0], outlineOfStates)):
					print "Found Tweet"
					hashtags = [] 
					milliseconds =int(tweet['timestamp_ms'])
					date = time.gmtime(milliseconds/1000.)
					
					try:
						#print "The date is: " + str(date[0]), str(date[1]), str(date[2])
						date = str(date[0])+"/"+str(date[1])+"/"+str(date[2])
						
					except: 
						date='No date'
					try:
						#print "The id is: " + str(tweet['id'])
						tweetid = str(tweet['id'])
						#Make sure no tweet is added twice
						if tweetid in tweetidList:
							continue
						else:
							tweetidList.append(tweetid)
					except:
						print "hit except case"
						tweetid='No Tweet ID'		
					try:
						if len(tweet['entities']['hashtags'])!=0:
							num = len(tweet['entities']['hashtags'])
							#print "The hashtags are: "
							string=""
							for x in range(num):
								#print tweet['entities']['hashtags'][x]['text'].encode('utf-8')
								string=string+tweet['entities']['hashtags'][x]['text'].encode('utf-8')+","
							stringOfHashtags=string
						
					except Exception,e:
						print e
						stringOfHashtags = 'No hashtags'			
					try:
						#print "The latitude is: " +str(tweet['geo']['coordinates'][0])
						latitude = str(tweet['geo']['coordinates'][0])
						
					except:
						latitude = "No Latitude"
					
					try:
						#print "The longitude is: " +str(tweet['geo']['coordinates'][1])
						longitude = str(tweet['geo']['coordinates'][1])
						
					except:	
						longitude = 'No Longitude'
					
					try:	
						#print "The text is: " + tweet['text'].encode('utf-8')
						tweettext = tweet['text'].encode('utf-8')

					except Exception,e:
						tweettext = 'No text'
					 
					#remove commas form text so can format easily in Excel
					try:
						noCommasInText = tweettext.replace(',',' ')
					except:
						noCommasInText='No text'
					
					try:
						noCommasInHashtags = hashtags.replace(',',' ')
					except:
						noCommasInHashtags='No hashtags'
					
		
					fileToWriteTo.write(tweetid+','+noCommasInText+','+noCommasInHashtags+','+latitude+','+longitude+'\n')
							
		except: 
			continue
		if tweet_count >= 1000:
			break
fileToWriteTo.close()	



	
