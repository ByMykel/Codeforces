#https://codeforces.com/contest/4/problem/A

n = int(input())
for i in range(n):
    w = input()
    if len(w) > 10:
        print(f"{w[0]}{len(w)-2}{w[-1]}")
    else:
        print(w)
