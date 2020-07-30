#https://codeforces.com/problemset/problem/492/B

n, l = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = max(min(a), l - max(a))
for i in range(n-1):
    ans = max(ans, (a[i+1]-a[i]) / 2)
print(ans)
