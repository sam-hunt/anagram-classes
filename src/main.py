'''
Created on 2/03/2015

@author: sjhunt 14216618
'''

from __future__ import print_function

import sys, time
from collections import defaultdict

def loadwords():
    f = open('../res/words.txt', 'r')
    allwords = f.read()
    f.close
    words = allwords.lower().split('\n')
    return words

keys = defaultdict(list)
words = loadwords()             #precondition: =split list of lower case words

starttime = time.time()

for word in words:
    hkey = hash(''.join(sorted(word)))
    keys[hkey].append(word)     #loop invariant: all words processed so far have been added to a new/existing anagram class

with open('../out/sorted.txt', 'w') as f:
    for k in sorted(keys, key=lambda k: len(keys[k]), reverse=True ):
        print (keys[k], file=f)
        print (keys[k])

endtime = time.time()
print ('/nTime taken: ' + (endtime - starttime) + ' seconds')
