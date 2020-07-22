#https://codeforces.com/problemset/problem/1263/A

t = int(input())
for _ in range(t):
    r, g, b = sorted(map(int, input().split()))
    ans = 0
    if b - g >= r:
        g += r
        ans = g
    elif b - g < r:
        tmp = b - g
        g += tmp
        r -= tmp
        ans = g
        if r > 1:
            ans += r//2
    print(ans)
