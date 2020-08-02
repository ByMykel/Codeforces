#https://codeforces.com/contest/1388

t = int(input())
for _ in range(t):
    n = int(input())
    x = (n+3) // 4
    print("9"*(n-x) + "8"*(x))
