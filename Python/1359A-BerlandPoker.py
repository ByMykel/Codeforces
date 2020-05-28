#https://codeforces.com/contest/1359/problem/A

import math
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    if m == 0:
        print(0)
    else:
        r = n//k
        if n == m:
            print(0)
        elif r >= m:
            print(m)
        elif r < m:
            print(r - math.ceil((m-r) / (k-1))) 
