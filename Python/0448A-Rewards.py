#https://codeforces.com/contest/448/problem/A

import math
a = sum(list(map(int, input().split())))
b = sum(list(map(int, input().split())))
n = int(input())
if math.ceil(a/5) + math.ceil(b/10) > n:
    print("NO")
else:
    print("YES")
