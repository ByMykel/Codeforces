#https://codeforces.com/problemset/problem/1316/A

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(min(sum(a), m))
