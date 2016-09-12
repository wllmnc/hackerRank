# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/funny-string
for i in xrange(int(raw_input())):
    ans="Funny"
    s=list(raw_input())
    for i in xrange(1,len(s)):
        if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(s[len(s)-i-1])-ord(s[len(s)-(i-1)-1])):
            ans="Not "+ans
            break
    print ans
