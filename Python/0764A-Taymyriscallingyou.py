#https://codeforces.com/problemset/problem/764/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, m, z = inm()
ans = 0
for i in range(1, z+1):
    if i % n == 0 and i % m == 0:
        ans += 1
print(ans)
