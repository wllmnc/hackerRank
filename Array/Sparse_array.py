#https://www.hackerrank.com/challenges/sparse-arrays
# Enter your code here. Read input from STDIN. Print output to STDOUT
aStrings=[]
aQueries=[]
answers={}

for i in range(int(raw_input())):
    aStrings.append(raw_input())
#get the queries
for i in range(int(raw_input())):   
    key=raw_input()
    aQueries.append(key)
    if not key in answers:
        count=0
        while key in aStrings:
            aStrings.remove(key)
            count=count+1
        answers[key]=count
for word in aQueries:
    print answers[word]
    
