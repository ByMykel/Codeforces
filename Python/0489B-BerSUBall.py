#https://codeforces.com/problemset/problem/489/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

n = ini()
a = sorted(inl())
m = ini()
b = sorted(inl())
ans = 0
start = 0
for i in a:
    for j in range(start, m):
        if abs(i - b[j]) <= 1:
            ans += 1
            start = j + 1
            break
print(ans)
