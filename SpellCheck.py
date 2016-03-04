#!/usr/bin/python
import enchant
import fileinput

d = enchant.Dict("en_US")

fname = raw_input("Enter file name : ")
f = fileinput.FileInput(fname, inplace=True)
	
for line in f:
	for word in line.split():
		if word[-1] == '?' or word[-1] == '!' or word[-1] == '.':
			word = word[:-1]
		if d.check(word) == False:
			line = line.replace(word,word + "(CHECK)")
	print line,
f.close()
