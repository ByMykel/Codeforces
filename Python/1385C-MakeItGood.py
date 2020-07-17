#https://codeforces.com/contest/1385/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    out = n - 1
    while out > 0:
        if a[out] <= a[out-1]:
            out -= 1
        else:
            break
    while out > 0:
        if a[out] >= a[out-1]:
            out -= 1
        else:
            break
    print(out)
