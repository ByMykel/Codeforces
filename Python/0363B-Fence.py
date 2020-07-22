#https://codeforces.com/problemset/problem/363/B

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
total = sum(a[:k])
count = total
l = 0
for i in range(k, n):
    total -= a[l]
    total += a[i]
    l += 1
    if total < count:
        count = total
        ans = l
print(ans + 1)
