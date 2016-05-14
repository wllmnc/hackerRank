#https://www.hackerrank.com/challenges/alternating-characters/submissions
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
ar=[raw_input() for _ in range(0,n)]

for string in ar:
    prev=string[0]
    cont=0
    for i in range(1,len(string)):
        current=string[i]
        cont=cont+(1 if prev==current else 0)
        prev=current
    print cont
    