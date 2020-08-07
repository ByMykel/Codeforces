#https://codeforces.com/problemset/problem/1204/B

n, l, r = map(int, input().split())
min = n - (l - 1)
tmp = 2
l -= 1
for i in range(l):
    min += tmp
    l -= 1
    if l > 0:
        tmp += tmp
max = 0
tmp = 1
for i in range(n):
    max += tmp
    r -= 1
    if r > 0:
        tmp += tmp
print(min, max)
