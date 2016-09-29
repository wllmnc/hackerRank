#https://www.hackerrank.com/challenges/the-love-letter-mystery
for _ in xrange(int(raw_input())):
    s=list(raw_input())
    movs=0
    for i in xrange(len(s)/2):
        char1,char2=s[i],s[len(s)-i-1]
        if char1!=char2:
            movs=movs+abs(ord(char2)-ord(char1))
    print movs
