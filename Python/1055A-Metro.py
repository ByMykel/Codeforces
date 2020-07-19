#https://codeforces.com/problemset/problem/1055/A

n, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[0] == 0:
    print("NO")
elif a[s-1] != 0:
    print("YES")
elif b[s-1] == 0:
    print("NO")
else:
    out = False
    for i in range(s, n):
        if a[i] + b[i] == 2:
            out = True
            break
    print("YES" if out else "NO")
