#https://codeforces.com/problemset/problem/1426/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, m = inm()
    ans = False
    for i in range(n):
        a = inl()
        b = inl()
        if a[1] == b[0]:
            ans = True
    if m % 2 != 0:
        ans = False
    print("YES" if ans else "NO")
