#https://codeforces.com/problemset/problem/248/A

n = int(input())
output = 0
lc, rc = 0, 0
for i in range(n):
    l, r = map(int, input().split())
    lc += l
    rc += r
print(min(lc, n-lc) + min(rc, n-rc))
