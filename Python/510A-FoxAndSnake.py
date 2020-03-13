#https://codeforces.com/contest/510/problem/A

n, m = map(int, input().split())
t = True
for i in range(1, n+1):
    if i % 2 == 0:
        if t :
            print("." * (m-1), end="")
            print("#")
            t = False
        else:
            print("#", end="")
            print("." * (m-1))
            t = True
    else:
        print("#" * m)
