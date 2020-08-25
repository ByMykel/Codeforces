#https://codeforces.com/problemset/problem/34/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n, m = inm()
a = sorted(inl())
ans = 0
for i in a:
    if m == 0:
        break
    if i <= 0:
        ans -= i
        m -= 1
print(ans)
