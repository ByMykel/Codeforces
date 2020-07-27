#https://codeforces.com/problemset/problem/987/B

import math
x, y = map(int, input().split())
a = y * math.log(x)
b = x * math.log(y)
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")
