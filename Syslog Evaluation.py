#!/usr/bin/venv python

import re

file = open("sysLog.txt", "r")

regex = re.compile(r'\b\w{9}\b')
#regex = re.match(r'\b\w{5}\b')

words = {}
count = 0
given_words = ['anonymous', 'guest', re.IGNORECASE]
for x in file.read().split():
    count += 1
    if x in given_words:
        words.setdefault(x, 0)
        words[str(x)] += 1
print(count, words)

file.close()
