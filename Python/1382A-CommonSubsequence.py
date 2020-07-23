#https://codeforces.com/problemset/problem/1382/A

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m < n:
        a, b = b, a
    out = False
    for i in a:
        if i in b:
            out = True
            break
    if out:
        print("YES")
        print(1, i)
    else:
        print("NO")
