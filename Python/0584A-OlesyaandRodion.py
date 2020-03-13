#https://codeforces.com/problemset/problem/584/A

n, t = map(int, input().split())
if n == 1 and t > 9:
    print("-1")
elif t == 10:
    print(str(1)*(n-1) + "0")
else:
    print(n * str(t))
