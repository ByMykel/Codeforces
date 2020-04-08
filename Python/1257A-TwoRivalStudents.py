#https://codeforces.com/problemset/problem/1257/A

t = int(input())
for i in range(t):
    n, x, a, b = map(int, input().split())
    if x == 0:
        print(abs(a - b))
    else:
        print(min(abs(a - b) + x, n-1))
