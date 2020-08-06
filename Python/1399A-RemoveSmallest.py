#https://codeforces.com/problemset/problem/1399/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = True
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            ans = False
            break
    print("YES" if ans else "NO")
