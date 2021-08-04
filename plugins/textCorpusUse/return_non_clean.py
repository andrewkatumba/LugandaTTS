import csv
import sys
import re

MAX_TOKENS = 14

ENGLISH = ['and', 'the', 'is']

matched = 0
total = 0

for line in sys.stdin:
	valid = True
	row = line.strip('\n').split('\t')
	text = row[0].strip()
	
	if len(text.split()) > MAX_TOKENS:
		matched +=1
		valid = False
	if re.findall('[0-9]', text):
		matched +=1
		valid = False
	if text == '':
		matched +=1
		valid = False

	foreign = False
	for token in text.split(' '):
		if token in ENGLISH:
			foreign = True
	if foreign:
		matched +=1
		valid = False

	if not valid:
		print('\t'.join(row))	
		total += 1

print('Total:', total, ', Matched:', matched, file=sys.stderr)
