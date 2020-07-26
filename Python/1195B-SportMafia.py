#https://codeforces.com/problemset/problem/1195/B

n, k = map(int, input().split())
ans = 0
cnt = 1
for i in range(n):
    ans += cnt
    cnt += 1
    if ans - (n-i-1) == k:
        print(n-i-1)
        break
