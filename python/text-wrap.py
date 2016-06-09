# https://www.hackerrank.com/challenges/text-wrap
# Enter your code here. Read input from STDIN. Print output to STDOUT
S,N=raw_input(),int(raw_input())
print S[i:i+N] for i in range(0,len(S),N):
    print S[i:i+N]
