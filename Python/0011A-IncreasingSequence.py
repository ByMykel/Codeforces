#https://codeforces.com/problemset/problem/11/A

import math
n, d = map(int, input().split())
b = list(map(int, input().split()))
prev = 0
output = 0
for i in range(n):
    if b[i] == prev:
        output += 1
        b[i] += d
    elif b[i] < prev:
        step = math.ceil((prev-b[i]) / d)
        output += step
        b[i] += d*step
        if b[i] == prev:
            b[i] += d
            output += 1
    prev = b[i]
print(output)
