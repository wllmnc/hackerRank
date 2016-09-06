# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/swap-case
ans=""
for s in raw_input():
    value=ord(s)
    if value>64 and value<91:
        value=value+32
    elif value>96 and value<123:
        value=value-32
    ans=ans+chr(value)
print ans
