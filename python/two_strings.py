# https://www.hackerrank.com/challenges/two-strings/
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
testcases=[]
for i in range(0,n):
    testcases.append((raw_input(),raw_input()))

for (subA,subB) in testcases:
    result="NO"
    for s in range(97,123):
        if chr(s) in subA and chr(s) in subB:
            result="YES"
            break    
    print result
        
        