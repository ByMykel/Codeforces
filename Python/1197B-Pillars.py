#https://codeforces.com/problemset/problem/1197/B

n = int(input())
a = list(map(int, input().split()))
if a == sorted(a) or a == sorted(a, reverse=True):
    print("YES")
else:
    out = True
    for i in range(n):
        if a[i] > a[i+1]:
            break
    for j in range(i, n-1):
        if a[j] < a[j+1]:
            out = False
            break
    print("YES" if out else "NO")
