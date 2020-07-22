#https://codeforces.com/problemset/problem/1263/A

t = int(input())
for _ in range(t):
    r, g, b = sorted(map(int, input().split()))
    ans = 0
    if r + g <= b:
        ans = r + g
    else:
        ans = (r+g+b) // 2
    print(ans)
