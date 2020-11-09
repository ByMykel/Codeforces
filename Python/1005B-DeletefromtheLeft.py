#https://codeforces.com/problemset/problem/1005/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

s = ins()
t = ins()
ans = 0
for i in range(1, min(len(s), len(t)) + 1):
    if s[-i] != t[-i]:
        break
    ans += 2
print(len(s) + len(t) - ans)
