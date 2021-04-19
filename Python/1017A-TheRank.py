#https://codeforces.com/problemset/problem/1017/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini() - 1
a = sum(inl())
ans = 1
for _ in range(t):
    b = sum(inl())
    if b > a:
        ans += 1
print(ans)
