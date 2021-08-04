import csv
import sys
import re

MAX_TOKENS = 14

ENGLISH = ['and', 'the', 'is']

skipped = 0
total = 0

for line in sys.stdin:
	row = line.strip('\n').split('\t')
	text = row[0].strip()
	
	if len(text.split()) > MAX_TOKENS:
		skipped +=1
		continue
	if re.findall('[0-9]', text):
		skipped +=1
		continue
	if text == '':
		skipped +=1
		continue
	foreign = False
	for token in text.split(' '):
		if token in ENGLISH:
			foreign = True
	if foreign:
		skipped +=1
		continue

	print('\t'.join(row))	
	total += 1

print('Valid:', total, ', Skipped:', skipped, file=sys.stderr)
