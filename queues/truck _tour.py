#https://www.hackerrank.com/challenges/truck-tour

# Enter your code here. Read input from STDIN. Print output to STDOUT
def getCyclePumpCost(nPumps,index,resumePetrol):
    completeCyle=True
    for i in xrange(1,int(a[0])-1):
        [pump,distance]=arr[(i+index)%len(arr)]
        resumePetrol=resumePetrol+pump-distance
        if resumePetrol<0:
                completeCyle=False
                break
    return completeCyle

a = map(int, raw_input().strip().split(" "))
arr=[]
for i in xrange(0,a[0]):
    arr.append(map(int, raw_input().strip().split(" ")))
numbersOfPumps=len(arr)
i=0
candidate=len(arr)

for row in arr:
    [pump,distance]=row
    if pump-distance> 0:
        completeCycle=getCyclePumpCost(1,i,pump-distance)
        if completeCycle :
            candidate=i
            break
    i=i+1
print candidate


    
    
