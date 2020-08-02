#https://codeforces.com/problemset/problem/1359/B

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    y = y if x*2 > y else x*2
    ans = 0
    for _ in range(n):
        s = list(filter(lambda x: x > 0, map(lambda x: len(x), input().split("*"))))
        for i in s:
            if i % 2 == 0:
                ans += i//2 * y
            else:
                ans += i//2 * y + x
    print(ans)
