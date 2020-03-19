#https://codeforces.com/contest/1326/problem/A

t = int(input())
for i in range(t):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        print("27" + "7"*(n-2))
