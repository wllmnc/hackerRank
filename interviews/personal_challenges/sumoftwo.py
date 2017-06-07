#https://codefights.com/interview/qAL6AiSejoJZRNyox
def sumOfTwo(a, b, v):
    ans=False
    i=0
    while i<len(a):
        item=a[i]
        if abs(v-item) in b:
            ans=True
            i=len(a) 
        i+=1
    return ans
        

