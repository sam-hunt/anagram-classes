'''
Created on 2/03/2015

@author: sjhunt 14216618
'''

import sys, time
from collections import defaultdict

def loadwords():
    f = open('words.txt', 'r')
    allwords = f.read()
    f.close
    words = allwords.lower().split('\n')
    return words
#===============================================================================
# 
# def hash3(word):                #4-byte folding string hash function
#     ilen, sum = len(word)/4, 0
#     for j in xrange(ilen):
#         subword = word[j*4:(j*4)+4]
#         mult, swl = 1, len(subword)
#         for k in xrange(swl):
#             sum += ord(subword[k]) * mult
#             mult *= 256
#     subword = word[ilen*4:]
#     mult = 1
#     for k in xrange(len(subword)):
#         sum += ord(subword[k])*mult
#         mult *= 256
#     return sum
#===============================================================================

keys = defaultdict(list)
words = loadwords()             #precondition: =split list of lower case words

starttime = time.time()

for word in words:
    hkey = hash(''.join(sorted(word)))
    keys[hkey].append(word)     #loop invariant: all words processed so far have been added to a new/existing anagram class

for k in sorted(keys, key=lambda k: len(keys[k]), reverse=True ):
    print keys[k]

endtime = time.time()
print endtime - starttime