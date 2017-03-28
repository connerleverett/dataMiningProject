'''
	This program removes both unneccesary puncuation and 'https', 't', and 'co', turns all words to lowercase, as well as removes common english stop words.
	Stop words taken from 'http://www.ranks.nl/stopwords'. 
'''

import re

# -------------Change input file name here-----------------
file = open('oneThousandTweets.txt', 'rt')
file2 = open('stopwords.txt', 'rt')
outputFile = open('noStopWords1000.txt', 'w')

D = []

for x in file:
	D.append(x.strip())
	
stopWords = ['https', 't', 'co']

for x in file2:
	stopWords.append(x.strip())
	
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
		elif (wordsInTweet[num] not in stopWords):
			cleanedTweet = cleanedTweet + ' ' + wordsInTweet[num]
	outputFile.write(cleanedTweet + '\n')

outputFile.close()