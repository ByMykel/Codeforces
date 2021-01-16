#https://codeforces.com/problemset/problem/1473/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, d = inm()
    a = sorted(inl())
    if a[-1] <= d or a[0] + a[1] <= d:
        print("YES")
    else:
        print("NO")
