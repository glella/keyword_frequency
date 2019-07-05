#!/usr/bin/env python3
# put target list of keywords in same directory in a column of a cvs file named target.csv
# provide plain text file named text.txt
# outputs another csv file named results.csv with the frequency of the target words

import csv
import codecs
import re
import collections

target = []

with codecs.open('target.csv', "r", encoding="utf-8-sig") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		target.append(row[0])

words = re.findall('\w+', open('text.txt').read().lower())

hashmap = { i : 0 for i in target }

for word in words:
	if word in hashmap:
		hashmap[word] = hashmap[word] + 1

for word in target:
    print('Word: ' + word + ' - Frequency: ' + str(hashmap[word]))

with open('results.csv','w') as f:
    w = csv.writer(f)
    w.writerows(hashmap.items())


