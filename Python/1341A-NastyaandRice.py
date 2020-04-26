#https://codeforces.com/problemset/problem/1341/A

t = int(input())
for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    if n * (a+b) >= c-d and n * (a-b) <= c+d:
        print("YES")
    else:
        print("NO")
