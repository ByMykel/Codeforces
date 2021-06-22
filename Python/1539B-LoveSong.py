#https://codeforces.com/problemset/problem/1539/B

import sys

input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s="\n": print(s.join(map(str, x)))

q, n = inm()
s = ins()
ans = [0] * (q + 1)
for i in range(1, q + 1):
    ans[i] += ans[i - 1] + ord(s[i - 1]) - 96
for _ in range(n):
    l, r = inm()
    print(ans[r] - ans[l - 1])
