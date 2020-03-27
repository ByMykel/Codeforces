#https://codeforces.com/problemset/problem/1328/A

import math
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(math.ceil(a/b) * b - a)
