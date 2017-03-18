import math
import re

#TODO: Make re to strip tweet of all it's punctuation and links
# DONE

#------For use in finding condition probability------
#Counts number of times a word shows up in the text label list e.g. text0
def countTokensOfTerm(textc, t):
	TCT = 0
	for x in textc:
		if t == x:
			TCT += 1
	return TCT
	
#------For use in finding index in condProb list------
def findIndexOfCondProb(t):
	index = 0
	for x in range(0, len(V)):
		if V[x] == t:
			index = x
			break
	return index
	
#
#------Train Multinomial NB-----------------------------------------------------------------------------------------------
#

#------Extracting from classes and docs from files------

file = open('trainlabels.txt', 'rt')
file2 = open('traindata.txt', 'rt')

C = []
D = []

# Takes each sentence and appends it to the list
for x in file:
	C.append(x.strip())
for x in file2:
	D.append(x.strip())

#------Extract vocabulary from D------
# splits each tweet into its component words
# V is a list with all the words used in the tweets including repitions
V = []
#numTermsInV is all unique words
numTermsInV = 0
for x in D:
	wordsInTweet = re.sub("[^\w']", " ",  x).split()
	for y in range(0, len(wordsInTweet)):
		if wordsInTweet[y] not in V:
			numTermsInV += 1
		V.append(wordsInTweet[y])

print V
#------Count the number of docs--------
# TODO: add two more counters (N2, N3)
# DONE
N = len(D)
N0 = 0
N1 = 0
N2 = 0
N3 = 0

# TODO: add two more checks for N2 and N3
# DONE
# This is counting the number of labels
for x in range(0, len(C)):
	if C[x] == '0':
		N0 += 1
	if C[x] == '1':
		N1 += 1
	if C[x] == '2':
		N2 += 1
	if C[x] == '3':
		N3 += 1


#------Tokenizer------
# TODO: add two more lists for text of type labels 2 and 3
# DONE
text0 = []
text1 = []
text2 = []
text3 = []
counter = 0

# breaks down tweet into words and places those words in appropriate list
# TODO: append into extra lists for extra labels
#DONE
for x in D:
	wordsInTweet = re.sub("[^\w']", " ",  x).split()
	if C[counter] == '0':
		for y in range(0, len(wordsInTweet)):
			text0.append(wordsInTweet[y])
	if C[counter] == '1':
		for y in range(0, len(wordsInTweet)):
			text1.append(wordsInTweet[y])
	if C[counter] == '2':
		for y in range(0, len(wordsInTweet)):
			text2.append(wordsInTweet[y])
	if C[counter] == '3':
		for y in range(0, len(wordsInTweet)):
			text3.append(wordsInTweet[y])
	counter += 1

# prior is a 2 item list that contains the condProb in each position for each label
prior = []
#this will need to be a list of 4 lists
condProb = [[],[], [], []]

#------Find condition probability------
# TODO: loop through 4 times instead of 2 (for each type of label)
# DONE

for c in range(0, 4):
	if c == 0:
		prior.insert(c, float(N0)/float(N))
	if c == 1:
		prior.insert(c, float(N1)/float(N))
	if c == 2:
		prior.insert(c, float(N2)/float(N))
	if c == 3:
		prior.insert(c, float(N3)/float(N))
	for t in range(0, len(V)):
		if c == 0:
			TCT = countTokensOfTerm(text0, V[t])
			prob = (float(TCT + 1)/(len(text0) + numTermsInV))
			condProb[0].insert(t, prob)
		if c == 1:
			TCT = countTokensOfTerm(text1, V[t])
			prob = (float(TCT + 1)/(len(text1) + numTermsInV))
			condProb[1].insert(t, prob)
		if c == 2:
			TCT = countTokensOfTerm(text2, V[t])
			prob = (float(TCT + 1)/(len(text2) + numTermsInV))
			condProb[2].insert(t, prob)
		if c == 3:
			TCT = countTokensOfTerm(text3, V[t])
			prob = (float(TCT + 1)/(len(text3) + numTermsInV))
			condProb[3].insert(t, prob)

#--------------------------------------------------------------------------------------------------------------------------------------------
#
#------Apply Multinomial NB------------------------------------------------------------------------------------------------------------------
#

'''
!NOTE!
IF YOU WANT TO CHANGE THE INPUT FILE THIS IS THE PLACE TO DO IT
SIMPLY SWITCH 'TRAIN...' WITH 'TEST...'
'''
file = open('trainlabels.txt', 'rt')
file2 = open('traindata.txt', 'rt')
#file = open('testlabels.txt', 'rt')
#file2 = open('testdata.txt', 'rt')

C = []
D = []

for x in file:
	C.append(x.strip())
for x in file2:
	D.append(x.strip())

#------Extract vocabulary from D------

# for accuracy 
right = 0
wrong = 0

#------Iterate through all docs------

#------Extract tokens from doc------
#------This for loop only extracts the words from the doc that are also in the Vocabulary------
# runs for every single tweet
for i in range(0, len(D)):
	#Breaks tweet up into component words
	doc = re.sub("[^\w']", " ",  D[i]).split()
	W = []
	#Check if word is in V
	for x in range(0, len(doc)):
		if doc[x] in V:
			W.insert(x, doc[x])
	
	#------For loop to compute conditional probability------
	score = []
	#TODO: add two more
	# DONE
	for c in range(0, 4):
		score.append(math.log(prior[c]))
		if c == 0:
			for t in W:
				index = findIndexOfCondProb(t)
				score[c] += math.log(condProb[c][index])
		if c == 1:
			for t in W:
				index = findIndexOfCondProb(t)
				score[c] += math.log(condProb[c][index])
		if c == 2:
			for t in W:
				index = findIndexOfCondProb(t)
				score[c] += math.log(condProb[c][index])
		if c == 3:
			for t in W:
				index = findIndexOfCondProb(t)
				score[c] += math.log(condProb[c][index])
	
	#------Test to check accuracy (Should be > 90%)------
	#TODO: check for 4 labels
	# DONE
	print score
	if score[0] > score[1] and score[0] > score[2] and score[0] > score[3]:
		if C[i] == '0':
			right += 1
		else:
			wrong += 1
	if score[1] > score[0] and score[1] > score[2] and score[1] > score[3]:
		if C[i] == '1':
			right += 1
		else:
			wrong += 1
	if score[2] > score[0] and score[2] > score[1] and score[2] > score[3]:
		if C[i] == '2':
			right += 1
		else:
			wrong += 1
	if score[3] > score[0] and score[3] > score[1] and score[3] > score[2]:
		if C[i] == '3':
			right += 1
		else:
			wrong += 1
print
print('Accuracy: ' + str((float(right)/(right+wrong))*100) + '%')
