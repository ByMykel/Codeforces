#https://codeforces.com/contest/1335/problem/A

t = int(input())
for i in range(t):
    n = int(input())
    if n < 3:
        print(0)
    else:
        if n % 2 == 0:
            print(n//2 - 1)
        else:
            print(n // 2)
