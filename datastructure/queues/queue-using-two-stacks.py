#https://www.hackerrank.com/challenges/queue-using-two-stacks
# Enter your code here. Read input from STDIN. Print output to STDOUT
stack1 = []

n=int(raw_input())
while(n>0):
    q=raw_input().split(" ")
    val=0 if len(q)<2 else int(q[1])
    query=int(q[0])
    if query==1:
        stack2 = stack1
        stack2.insert(0,val)
        stack1 = stack2
        stack2 = []
    elif query==2:
        if len(stack1)>0:
            stack1.pop()
    else:
        if len(stack1)>0:
            print stack1[len(stack1)-1]
    n=n-1
        
