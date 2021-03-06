#https://www.hackerrank.com/challenges/candies
n = input()
a = [input() for _ in xrange(n)]
c, desc_buf = [1]*n, []

for i in xrange(1, n):
    if a[i] < a[i-1]:
        if not desc_buf:
            desc_buf = [i-1]
        desc_buf.append(i)
        if not i == n-1:
            continue
    if a[i] > a[i-1]:
        c[i] = c[i-1] + 1
    if desc_buf:
        for extra, idx in enumerate(desc_buf[::-1]):
            c[idx] = max(c[idx], extra + 1)
        del desc_buf[:]

print sum(c)
