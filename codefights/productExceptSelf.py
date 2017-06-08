#https://codefights.com/interview/Bpdq6EYZ6MW586va3
def productExceptSelf(nums, m):
    total=1
    for i in range(len(nums)):
        total*=nums[i]
    arr_=[ (total/nums[i])%m for i in range(len(nums))   ]
    return sum(arr_)%m

