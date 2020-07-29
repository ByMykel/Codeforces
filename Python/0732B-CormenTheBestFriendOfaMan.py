#https://codeforces.com/problemset/problem/732/B

n, k = map(int, input().split())
a = list(map(int ,input().split()))
ans = sum(a)
for i in range(n-1):
    if a[i] + a[i+1] < k:
        a[i+1] += k - (a[i] + a[i+1])
print(sum(a) - ans)
print(*a)
