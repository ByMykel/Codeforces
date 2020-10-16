#https://codeforces.com/problemset/problem/919/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, m = inm()
ans = 1e9
for _ in range(n):
    a, b = inm()
    ans = min(ans, m*a / b)
print(ans)
