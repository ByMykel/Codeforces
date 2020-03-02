#https://codeforces.com/contest/1311/problem/A

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    elif a > b and (a - b) % 2 == 0:
        print(1)
    elif a < b and (b - a) % 2 != 0:
        print(1)
    else:
        print(2)
