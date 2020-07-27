#https://codeforces.com/problemset/problem/1139/B

n = int(input())
a = list(map(int, input().split()))
prev = a[n-1]
count = prev
ans = count
for i in range(n-2, -1, -1):
    if a[i] < prev:
        count += a[i]
        ans = max(ans, count)
        prev = a[i]
    else:
        count += prev - 1
        ans = max(ans, count)
        prev = prev - 1
    if a[i] == 1:
        count = 0
print(ans)
