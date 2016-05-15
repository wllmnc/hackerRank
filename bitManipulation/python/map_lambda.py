#https://www.hackerrank.com/challenges/map-and-lambda-expression/
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())

fibo=lambda a: fibo(a-1)+fibo(a-2) if a>1 else (0 if a==0 else 1)
cubeFibo=lambda a: pow(fibo(a),3)
ar=map(cubeFibo,range(0,n))
print ar