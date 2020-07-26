#https://codeforces.com/contest/805/problem/B

import math
n = int(input())
s = "aabb" * math.ceil(n/4)
print(s[:n])
