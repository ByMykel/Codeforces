#https://codeforces.com/problemset/problem/1445/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for i in range(t):
    n, x = inm()
    a = sorted(inl())
    b = sorted(inl(), reverse=True)
    if (i + 1 != t):
        ins()
    ans = True
    for i in range(n):
        if a[i] + b[i] > x:
            ans = False
            break
    print("Yes" if ans else "No")
