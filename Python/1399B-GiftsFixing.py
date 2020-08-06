#https://codeforces.com/contest/1399/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    amin = min(a)
    bmin = min(b)
    ans = 0
    for i in range(n):
        ans += max(a[i] - amin, b[i] - bmin)
    print(ans)
