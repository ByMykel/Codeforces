#https://codeforces.com/problemset/problem/1398/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

ans = []
t = ini()
for _ in range(t):
    n = ini()
    a = inl()
    out = False
    i = 0
    j = 2
    while j < n:
        if a[i] + a[i+1] <= a[j]:
            out = True
            break
        else:
            j += 1
    if out:
        ans.append(f"{i+1} {i+2} {j+1}")
    else:
        ans.append("-1")
print('\n'.join(ans))
