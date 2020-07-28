#https://codeforces.com/contest/339/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split())) + [0]
ans = 0
prev = 0
for i in range(m+1):
    if prev > a[i]:
        if a[i] == 0:
            ans += a[i-1]
        else:
            ans += n
    prev = a[i]
print(ans - 1)
