'''
	This uses a stratified 10-fold cross validation for testing accuracy.
	TODO:
	You need to count how many of each type of label there are and stratify it so there is no bias.
	As in:
	for 0 there is 335
	1 is 660
	2 is 373
	3 is 680
	stratified (rounded down)
	33 tweets for 0
	66 tweets for 1
	37 tweets for 2
	68 tweets for 3
	
	First step: split data into 10 subsets of equal size
		- find number of tweets of each type and divide by 10 (round down), then you'll find how many tweets you'll need from each label
			- Keep track of where in the list you've taken the tweets from (so you know where to go back to when iterating)
	Second step: use each subset in turn for testing, the remainder for training
		- insert that number of tweets from each label type into a new list which contains your test tweets
		compile the rest of the tweets into a list which is the tweets you'll train on
		
		loop through data, compile 4 seperate lists where each list item is another list item containing the tweets you're going to 
'''
import math
import re
import time
	
#
#------Train Multinomial NB-----------------------------------------------------------------------------------------------
#

#----------------------------------------------This section will categorize the tweets so we can apply cross validation-------------------------------------------
startTime = time.time()

#------Extracting from classes and docs from files------

#This is the classification
#file = open('nsweClassification.txt', 'rt')
# These are the tweets
#file2 = open('cleanedTrainData.txt', 'rt')

#This is for testing
file = open('test48Classification.txt', 'rt')
# These are the tweets
file2 = open('test48Tweets.txt', 'rt')

#tweetLengths = open("CorrectLengths.txt", "w")

C = []
D = []

# Takes each sentence and appends it to the list
for x in file:
	C.append(int(x.strip()))
for x in file2:
	D.append(x.strip())

# length of 48 for states in contiguous usa
tweets = []
labels = []
for x in range(0, 48):
	tweets.append([])
	labels.append([])

#------Count the number of training docs--------
# N is now numLabels
numLabels = 0
# N now represents a list where each index specifices that classifications length
N = [0] * 48
print "Count the number of labels and tweets"
# This is counting the number of labels
# This also places tweets and labels into new lists so they can be easily stratified and iterated over
for x in range(0, len(C)):
	if D[C[x]] == '':
		continue
	numLabels += 1
	N[C[x]] += 1
	tweets[C[x]].append(D[x])
	labels[C[x]].append(C[x])


print "Counted number of labels and tweets"
print
print "Start cross validation"
accuracySum = 0
subset = [0] * 48
for x in range(0, 48):
	subset[x] = N[x] / 10


#--------------------------------Start cross validation-------------------------------------------
for k in range(0, 10):
	print
	print "New fold"
	trainingTweets = []
	trainingLabels = []
	testingTweets = []
	testingLabels = []
	print
	print "appending into trainingTweets and trainingLabels"
	# Append into trainingTweets and trainingLabels
	for x in range(0, len(subset)):
		for y in range(0, k * subset[x]):
			trainingTweets.append(tweets[y])
			trainingLabels.append(labels[y])
		
	for x in range(0, k * subset1):
		trainingTweets.append(tweets1[x])
		trainingLabels.append(labels1[x])
		
	for x in range(0, k * subset2):
		trainingTweets.append(tweets2[x])
		trainingLabels.append(labels2[x])
		
	for x in range(0, k * subset3):
		trainingTweets.append(tweets3[x])
		trainingLabels.append(labels3[x])

	# Append into testingTweets and testingLabels
	for x in range(k * subset0, (k + 1) * subset0):
		testingTweets.append(tweets0[x])
		testingLabels.append(labels0[x])

	for x in range(k * subset1, (k + 1) * subset1):
		testingTweets.append(tweets1[x])
		testingLabels.append(labels1[x])

	for x in range(k * subset2, (k + 1) * subset2):
		testingTweets.append(tweets2[x])
		testingLabels.append(labels2[x])
		
	for x in range(k * subset3, (k + 1) * subset3):
		testingTweets.append(tweets3[x])
		testingLabels.append(labels3[x])

	# Append into trainingTweets and trainingLabels	
	for x in range((k + 1) * subset0, len(tweets0)):
		trainingTweets.append(tweets0[x])
		trainingLabels.append(labels0[x])
		
	for x in range((k + 1) * subset1, len(tweets1)):
		trainingTweets.append(tweets1[x])
		trainingLabels.append(labels1[x])
		
	for x in range((k + 1) * subset2, len(tweets2)):
		trainingTweets.append(tweets2[x])
		trainingLabels.append(labels2[x])
		
	for x in range((k + 1) * subset3, len(tweets3)):
		trainingTweets.append(tweets3[x])
		trainingLabels.append(labels3[x])
	print "Appended into trainingTweets and labels"
	print
	
	# ---------------------------END OF SECTION FOR CROSS VALIDATION-------------------------------------------------------------
	'''
	#----------------------------START TRAINING-----------------------------------------------------------	
		
	#------Extract vocabulary from trainingTweets and place into V and other appropriate list------
	# splits each tweet into its component words

	# V is a list with all the words used in the tweets including repititions
	V = {}
	vDict = {}
	countV = {}
	lengthV = 0

	text0 = {}
	lengthText0 = 0
	text1 = {}
	lengthText1 = 0
	text2 = {}
	lengthText2 = 0
	text3 = {}
	lengthText3 = 0
	counter = 0
	index = 0
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
	# N is the number of traingingTweets and N# is the number of trainingTweets of that label type
	N = len(trainingTweets)
	N0 = 0
	N1 = 0
	N2 = 0
	N3 = 0
	print "Fill V and count number of unique terms"
	# numTermsInV is all unique words
	numTermsInV = 0
	for x in trainingTweets:
		if trainingLabels[counter] == '0':
			N0 += 1
		elif trainingLabels[counter] == '1':
			N1 += 1
		elif trainingLabels[counter] == '2':
			N2 += 1
		elif trainingLabels[counter] == '3':
			N3 += 1
		wordsInTweet = x.split()
		for y in range(0, len(wordsInTweet)):
			try:
				countV[wordsInTweet[y]] = countV[wordsInTweet[y]] + 1
			except:
				countV[wordsInTweet[y]] = 1
				numTermsInV += 1
			#V.append(wordsInTweet[y])
			lengthV += 1
			V[index] = wordsInTweet[y]
			vDict[wordsInTweet[y]] = index
			if trainingLabels[counter] == '0':
				lengthText0 += 1
				#if wordsInTweet[y] in text0:
				try:
					text0[wordsInTweet[y]] = text0[wordsInTweet[y]]+1
				except:
					text0[wordsInTweet[y]]=1
			elif trainingLabels[counter] == '1':
				lengthText1 += 1
				try:
					text1[wordsInTweet[y]] = text1[wordsInTweet[y]]+1
				except:
					text1[wordsInTweet[y]]=1
			elif trainingLabels[counter] == '2':
				lengthText2 += 1
				try:
					text2[wordsInTweet[y]] = text2[wordsInTweet[y]]+1
				except:
					text2[wordsInTweet[y]]=1
			elif trainingLabels[counter] == '3':
				lengthText3 += 1
				try:
					text3[wordsInTweet[y]] = text3[wordsInTweet[y]]+1
				except:
					text3[wordsInTweet[y]]=1
			index += 1
		counter += 1

	print "Extracted vocabulary from trainingTweets and placed into appropriate lists"
	print numTermsInV
	print
	
	# loop through the rest of the code 10 times, changing the training and testing data each time

	# prior is a 2 item list that contains the condProb in each position for each label
	prior = []
	prior.insert(0, float(N0)/float(N))
	prior.insert(1, float(N1)/float(N))
	prior.insert(2, float(N2)/float(N))
	prior.insert(3, float(N3)/float(N))
	
	#this will need to be a list of 4 lists
	condProb = [[], [], [], []]

	#------Find condition probability------
	print "Find conditional probability"
	
	preTime = time.time()
	
	for t in range(0, lengthV):
		TCT = 0
		
		try:
			TCT = text0[V[t]]
		except:
			TCT = 0
		prob = (float(TCT + 1)/(lengthText0 + numTermsInV))
		condProb[0].insert(t, prob)
		
		try:
			TCT = text1[V[t]]
		except:
			TCT = 0
		prob = (float(TCT + 1)/(lengthText1 + numTermsInV))
		condProb[1].insert(t, prob)
		
		try:
			TCT = text2[V[t]]
		except:
			TCT = 0	
		prob = (float(TCT + 1)/(lengthText2 + numTermsInV))
		condProb[2].insert(t, prob)
		
		try:
			TCT = text3[V[t]]
		except:
			TCT = 0
		prob = (float(TCT + 1)/(lengthText3 + numTermsInV))
		condProb[3].insert(t, prob)
	
	print "Found conditional probability"
	print "Took", str(time.time() - preTime) +  "s to run"
	print ""

	
	#--------------------------------------------------------------------------------------------------------------------------------------------
	#
	#------Apply Multinomial NB------------------------------------------------------------------------------------------------------------------
	#
	print "Applying multinomial NB"

	# for accuracy 
	right = 0
	wrong = 0

	#------Iterate through all tweets from testingTweets------
	print "Iterating through all of the testingTweets"
	#------Extract words from tweet------
	#------This for loop only extracts the words from the wordsInTweet that are also in the Vocabulary------
	# runs for every single tweet in testingTweets
	counter = 0
	for x in testingTweets:
		# Breaks tweet up into component words
		wordsInTweet = x.split()
		W = {}
		# Check if word is in V
		for y in range(0, len(wordsInTweet)):
			try:
				W[y] = vDict[wordsInTweet[y]]
			except:
				continue
		
		#------For loop to compute conditional probability------
		score = []
		
		score.append(math.log(prior[0]))
		score.append(math.log(prior[1]))
		score.append(math.log(prior[2]))
		score.append(math.log(prior[3]))
		for t in W:
			score[0] += math.log(condProb[0][W[t]])
			score[1] += math.log(condProb[1][W[t]])
			score[2] += math.log(condProb[2][W[t]])
			score[3] += math.log(condProb[3][W[t]])

#------Test to check accuracy-------------------------------------------------------------------------------------------------------------------
		if score[0] > score[1] and score[0] > score[2] and score[0] > score[3]:
			if testingLabels[counter] == '0':
				tweetLengths.write(str(len(testingTweets[counter].split())) + "\n")
				right += 1
			else:
				wrong += 1
		elif score[1] > score[0] and score[1] > score[2] and score[1] > score[3]:
			if testingLabels[counter] == '1':
				tweetLengths.write(str(len(testingTweets[counter].split())) + "\n")
				right += 1
			else:
				wrong += 1
		elif score[2] > score[0] and score[2] > score[1] and score[2] > score[3]:
			if testingLabels[counter] == '2':
				tweetLengths.write(str(len(testingTweets[counter].split())) + "\n")
				right += 1
			else:
				wrong += 1
		elif score[3] > score[0] and score[3] > score[1] and score[3] > score[2]:
			if testingLabels[counter] == '3':
				tweetLengths.write(str(len(testingTweets[counter].split())) + "\n")
				right += 1
			else:
				wrong += 1
		
		counter += 1

	print('Accuracy: ' + str((float(right)/(right+wrong))*100) + '%')
	accuracySum += (float(right)/(right+wrong))*100
	
print
print "Total accuracy: " + str(accuracySum / 10) + "%"
tweetLengths.close()
print "Took", str(time.time() - startTime) +  "s to run"
'''