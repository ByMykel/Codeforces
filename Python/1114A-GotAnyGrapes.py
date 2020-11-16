#https://codeforces.com/problemset/problem/1114/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

x, y, z = inm()
a, b, c = inm()
ans = True
if a < x:
    ans = False
if a - x + b < y:
    ans = False
if a - x + b - y + c < z:
    ans = False
print("YES" if ans else "NO")
