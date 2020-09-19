#https://codeforces.com/problemset/problem/455/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = inl()
m = max(a) + 1
count = [0] * m
for i in a:
    count[i] += i
ans = [0] * m
for i in range(1, m):
    ans[i] = count[i]
    if i - 2 >= 0:
        ans[i] += ans[i-2]
    ans[i] = max(ans[i], ans[i-1])
print(ans[m-1])
