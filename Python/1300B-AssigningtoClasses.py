#https://codeforces.com/problemset/problem/1300/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(a[n] - a[n-1])
