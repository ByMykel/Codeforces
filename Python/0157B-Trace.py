#https://codeforces.com/problemset/problem/157/B

import math
n = int(input())
a = sorted(list(map(int, input().split())))
pi = math.pi
ans = 0
k = 1
for i in range(n-1, -1, -1):
    ans += k * a[i]**2 * pi
    k = -k
print(ans)
