#https://codeforces.com/problemset/problem/499/B

n, m = map(int, input().split())
words = {}
for _ in range(m):
    a, b = map(str, input().split())
    if len(a) < len(b) or len(a) == len(b):
        words[b] = a
    else:
        words[a] = b
a = list(map(str, input().split()))
for i in range(n):
    if a[i] in words:
        a[i] = words[a[i]]
print(*a)
