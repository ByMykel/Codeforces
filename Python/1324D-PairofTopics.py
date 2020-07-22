#https://codeforces.com/problemset/problem/1324/D

from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n
for i in range(n):
    c[i] = a[i] - b[i]
c = sorted(c)
ans = 0
for i in range(n):
    j = n - bisect_left(c, -c[i]+1, i+1, n)
    ans += j
print(ans)
