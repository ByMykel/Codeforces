#https://codeforces.com/problemset/problem/746/A

import sys
input = sys.stdin.readline
ini = lambda: int(input().rstrip())

a = ini()
b = ini()
c = ini()
print(7 * min(a, b//2, c//4))
