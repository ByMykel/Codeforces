#https://codeforces.com/problemset/problem/1354/A

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    if b >= a:
        print(b)
    elif b < a and d >= c:
        print(-1)
    elif b < a and c > d:
        print(b + (a-b + c-d - 1)//(c-d) * c)
