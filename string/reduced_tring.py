# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/reduced-string
s=raw_input()
for i in range(len(s)):
    for i in range(97,123):
        while chr(i)+chr(i) in s:
            s=s.replace(chr(i)+chr(i),"")
print s if len(s)>0 else "Empty String"
