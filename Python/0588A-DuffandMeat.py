#https://codeforces.com/problemset/problem/588/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
a = [0] * t
p = [0] * t
ans = 0
prev = 100
for i in range(t):
    a[i], p[i] = inm()
for i in range(t):
    prev = min(prev, p[i])
    ans += a[i] * prev
print(ans)
