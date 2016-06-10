# https://www.hackerrank.com/challenges/capitalize
boolSpace=True
S=raw_input()
output=""
for i in xrange(0,len(S)):
    char=S[i]
    if boolSpace and char!=" ":
        output=output+str(char.upper())
        boolSpace=False
    else:
        output=output+str(char)
        if char==" ":
            boolSpace=True
print output
    