#https://codeforces.com/problemset/problem/1358/A

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print((n*m+1) // 2)
