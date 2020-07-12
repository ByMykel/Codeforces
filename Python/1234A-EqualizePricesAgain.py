#https://codeforces.com/problemset/problem/1234/A

import math
q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(math.ceil(sum(a) / n))
