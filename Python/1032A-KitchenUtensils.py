#https://codeforces.com/contest/1032/problem/A

import math
n, k = map(int, input().split())
a = list(map(int, input().split()))
u = {}
for i in a:
    if i not in u:
        u[i] = 1
    else:
        u[i] += 1
print(math.ceil(max(u.values())/k) * len(u.keys()) * k - n)
