# https://www.hackerrank.com/challenges/making-anagrams
stringA,stringB=list(raw_input()),list(raw_input())
count=0
for char in stringA:
    if char in stringB:
        stringB.remove(char)
    else:
        count=count+1
print str(len(stringB)+count)
