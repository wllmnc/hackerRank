#https://www.hackerrank.com/challenges/py-introduction-to-sets
def average(array):
    # your code goes here
    setArray=set(array)
    sumT=0
    for item in setArray:
        sumT+=item
    return sumT/len(setArray)
