'''
Created on 8/03/2015

@author: Sam Hunt
'''
def hash2(word):                #just use alphabetically sorted words as keys
    sword, wordlen, hsum = ''.join(sorted(word)), len(word), 0
    for i in xrange(wordlen):
        hsum += (ord(sword[i])-95) * (ord(sword[i-1])-95)  
        return hsum

print hash2("a")
print hash2("aa")
print hash2("aaa")
print hash2("ab")

def hash3(word):
    ilen, sum = len(word)/4, 0
    for j in xrange(ilen):
        subword = word[j*4:(j*4)+4]
        mult, swl = 1, len(subword)
        for k in xrange(swl):
            sum += ord(subword[k]) * mult
            mult *= 256
    subword = word[ilen*4:]
    mult = 1
    for k in xrange(len(subword)):
        sum += ord(subword[k])*mult
        mult *= 256
    return sum

print hash3("a")
print hash3("aa")
print hash3("aaa")
print hash3("ab")
