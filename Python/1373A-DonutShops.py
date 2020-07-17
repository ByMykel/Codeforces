#https://codeforces.com/problemset/problem/1373/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a >= c:
        print(-1, end=" ")
    else:
        print(1, end=" ")
    if a*b <= c:
        print(-1)
    else:
        print(b)
