"Input have to be an matrix of n,n values with format of array of arrays"
"This funtion return the array in 2D with the required format"
def getSnailArray(arr):
    n=len(arr)
    ans=[]
    limit=0
    i,j=0,0
    while limit<n/2:
        i,j=limit,limit
        for i in range(limit,n-limit-1):
            ans.append(arr[j][i])
        for j in range(limit,n-limit-1):
            ans.append(arr[j][i+1])
        for i in range(limit,n-limit-1):
            ans.append(arr[j+1][n-i-1])
        for j in range(limit,n-limit-1):
            ans.append(arr[n-j-1][limit])
        limit=limit+1
    if n>0:
        ans.append(arr[j][i])
    return ans
