#https://codeforces.com/problemset/problem/1333/A

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    for i in range(n-1):
        print("W" + "B" * (m-1))
    print("B" * m)
