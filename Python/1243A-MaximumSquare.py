#https://codeforces.com/problemset/problem/1243/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n = ini()
    a = sorted(inl())
    ans = 1
    for i in range(n):
        ans = max(ans, min(i + 1, a[-i-1]))
    print(ans)
