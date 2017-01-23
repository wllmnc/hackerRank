#https://www.hackerrank.com/challenges/equality-in-a-array
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
ar=map(int,raw_input().split(" "))
items={}
for item in ar:
    if item in items:
        items[item]=items[item]+1
    else:
        items[item]=1        
max_=0;
for key_ in items:
    if items[key_]>max_:
        max_=items[key_];
print n-max_
