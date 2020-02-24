#https://codeforces.com/contest/1304/problem/A

n = int(input())
for i in range(n):
    x, y, a, b = map(int, input().split())
    if (y-x) % (a+b) == 0:
        print(int((y-x) / (a+b)))
    else:
        print(-1)
