#https://codeforces.com/problemset/problem/1230/A

a = sorted(list(map(int, input().split())))
if a[3] == sum(a) - a[3]:
    print("YES")
elif a[3] + a[0] == a[2] + a[1]:
    print("YES")
else:
    print("NO")
