# https://www.hackerrank.com/challenges/security-tutorial-functions
def  function1( x):
    return x%11

# https://www.hackerrank.com/challenges/security-function-ii/
def  function2( x):
    return pow(x,2)

# https://www.hackerrank.com/challenges/security-bijective-functions
def isBijective(y):
    oto=[]
    for item in y:
        if oto.__contains__(item):
            return "NO"
            
        oto.append(item)
    return "YES"

def mainBijective():
	n=raw_input()
	y=map(int,raw_input().split())

	print isBijective(y)