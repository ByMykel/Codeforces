#https://codeforces.com/problemset/problem/500/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, t = inm()
a = inl()
ans = False
i = 0
while True:
    if i > t-1:
        ans = False
        break
    if i == t-1:
        ans = True
        break
    i += a[i]
print("YES" if ans else "NO")
