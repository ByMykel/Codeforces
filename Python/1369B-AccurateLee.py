#https://codeforces.com/contest/1369/problem/B

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
    s = ins()
    start = 0
    end = 0
    for i in range(n):
        if s[i] == "0":
            start += 1
        else:
            break
    for i in range(n-1, -1, -1):
        if s[i] == "1":
            end += 1
        else:
            break
    if start + end == n:
        ans.append(s)
    else:
        ans.append("0"*start + "0" + "1"*end)
print('\n'.join(ans))
