'''
	This program removes both unneccesary punctuation and 'https', 't', and 'co', as well as turns all words into lower case. 
'''

import re

# -------------Change input file name here-----------------
file = open('trainTest.txt', 'rt')
outputFile = open('cleanedTrainData.txt', 'w')

D = []

for x in file:
	D.append(x.strip())
	
url = ['https', 't', 'co']
	
V = []
#numTermsInV is all unique words
numTermsInV = 0
for x in D:
	x = x.lower()
	wordsInTweet = re.sub("[^\w']", " ",  x).split()
	cleanedTweet = ''
	for num in range(0, len(wordsInTweet)):
		if (wordsInTweet[num] == 'co'):
			if (wordsInTweet[num - 1] != 't'):
				cleanedTweet = cleanedTweet + ' ' + wordsInTweet[num]
		elif (wordsInTweet[num] not in url):
			cleanedTweet = cleanedTweet + ' ' + wordsInTweet[num]
	outputFile.write(cleanedTweet + '\n')

outputFile.close()