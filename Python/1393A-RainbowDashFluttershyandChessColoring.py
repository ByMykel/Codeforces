#https://codeforces.com/problemset/problem/1393/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: tuple(map(int, input().split()))

ans = []
t = ini()
for i in range(t):
    n = ini()
    ans.append(n//2 + 1)
print('\n'.join(map(str, ans)))
