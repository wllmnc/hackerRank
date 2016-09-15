# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w23/challenges/treasure-hunting
(x,y),(a,b)=map(float,raw_input().split()),map(float,raw_input().split())
ab,bb=-b,a
print str((x*bb-ab*y)/(a*bb-ab*b))+"\n"+str((y-(((x*bb-ab*y)/(a*bb-ab*b))*b))/bb)
