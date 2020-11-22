#https://codeforces.com/contest/1452/problem/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

ans = []
t = ini()
for _ in range(t):
    x, y = inm()
    if x == y:
        ans.append(x + y)
    else:
        ans.append((max(x, y) - 1) * 2 + 1)
out(ans)
