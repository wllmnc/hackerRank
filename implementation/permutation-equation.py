# https://www.hackerrank.com/challenges/permutation-equation
n = int(raw_input())
p_temp = map(int, raw_input().split())
p = {v: k+1 for k, v in enumerate(p_temp)}
for i in range(1, n+1):
    print p[p[i]]
