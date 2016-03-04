#!/usr/bin/python
import fileinput

fname = raw_input("Enter file name : ")
f = fileinput.FileInput(fname, inplace=True)
for line in f:
	for word in line.split():
		if word[-1] == '?' or word[-1] == '!' or word[-1] == '.':
			word = word[:-1]
		if word[-7:] == '(CHECK)':
			origword = word[:-7]
			line = line.replace(word,origword)
	print line,
f.close()
