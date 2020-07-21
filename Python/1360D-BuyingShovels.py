#https://codeforces.com/contest/1360/problem/D

import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    out = n
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i <= k:
                out = min(out, n//i)
            if n//i <= k:
                out = min(out, i)
        i += 1
    print(out)
