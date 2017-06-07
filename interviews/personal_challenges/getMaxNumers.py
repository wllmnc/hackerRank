def getMaxNumers(arr_):
    if(len(arr_)<3):
        return 0,0,0
    arr_.sort()
    result=[arr_[len(arr_)-1],arr_[len(arr_)-2],arr_[len(arr_)-1]]
    if(arr_[0]<0):
        if(arr_[1]<0):
            result=[arr_[0],arr_[1],arr_[len(arr_)-1]] if arr_[0]*arr_[1]>arr_[len(arr_)-2]*arr_[len(arr_)-3] else [arr_[len(arr_)-2],arr_[len(arr_)-3],arr_[len(arr_)-1]]
    return result

arr_=[-100, -5, -1, 0, 1, 3, 6]
print getMaxNumers(arr_)
