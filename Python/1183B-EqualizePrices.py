#https://codeforces.com/problemset/problem/1183/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if min(a) + k >= max(a) - k:
        print(min(a) + k)
    else:
        print(-1)
