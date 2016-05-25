# https://www.hackerrank.com/challenges/word-order
apearOrder=[]
dicWords={}
for i in xrange(long(raw_input())):
    word=raw_input().replace("\r","")
    if not word in dicWords:
        apearOrder.append(word)
    dicWords[word]=1 if not word in dicWords else dicWords[word]+1
    

print len(apearOrder)
for word in apearOrder:
    print dicWords[word],