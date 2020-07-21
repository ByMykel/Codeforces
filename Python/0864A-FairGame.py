#https://codeforces.com/problemset/problem/864/A

n = int(input())
if n % 2 == 1:
    print("NO")
else:
    out = True
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    a = sorted(a)
    if a[0] != a[n//2-1]:
        out = False
    if a[n//2] != a[n-1]:
        out = False
    if a[0] == a[n-1]:
        out = False
    if out:
        print("YES")
        print(a[0], a[n-1])
    else:
        print("NO")
