#https://codeforces.com/contest/1/problem/A

import math
n, m, a = map(int, input().split())
print(math.ceil(n/a) * math.ceil(m/a))
