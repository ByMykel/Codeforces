#https://codeforces.com/problemset/problem/1516/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, k = inm()
    a = inl()
    for i in range(n - 1):
        x = min(k, a[i])
        a[i] -= x
        k -= x
        a[-1] += x
    print(*a)
