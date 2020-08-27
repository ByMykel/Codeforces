#https://codeforces.com/problemset/problem/1401/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

ans = []
t = ini()
for _ in range(t):
    n = ini()
    a = inl()
    b = sorted(a)
    m = min(a)
    tmp = True
    for i in range(n):
        if a[i] != b[i] and a[i] % m != 0:
            tmp = False
            break
    ans.append("YES" if tmp else "NO")
out(ans)
