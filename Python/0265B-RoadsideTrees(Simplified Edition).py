#https://codeforces.com/problemset/problem/265/B

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
ans = 0
prev = 0
for i in range(n):
    if prev >= a[i]:
        ans += 2 + prev - a[i]
    else:
        ans += 2 + a[i] - prev
    prev = a[i]
print(ans - 1)
