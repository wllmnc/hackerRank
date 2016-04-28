# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
array = sys.stdin.readlines()
numTestCases=int(array[0])
testCases=[]
for i in range(0,numTestCases):
     testCases.append(array[i*2+2].replace("\n","").split(" "));


for testCase in testCases:
    #print testCase
    result=0
    lim=len(testCase)
    if len(testCase)%2 == 1:
        for i in range(0,lim):
            if (i+1)%2==1:
                result=result^int(testCase[i])

    print result