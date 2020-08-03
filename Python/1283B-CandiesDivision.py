#https://codeforces.com/problemset/problem/1283/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ans = n//k * k + min(k//2, n % k)
    print(ans)
