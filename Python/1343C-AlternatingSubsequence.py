#https://codeforces.com/problemset/problem/1343/C

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
    count = 0
    tmp = a[0]
    prev = True if a[0] > 0 else False
    for i in range(1, n):
        actual = True if a[i] > 0 else False
        if actual == prev:
            tmp = max(tmp, a[i])
        else:
            count += tmp
            tmp = a[i]
        prev = actual
    ans.append(count + tmp)
out(ans)
