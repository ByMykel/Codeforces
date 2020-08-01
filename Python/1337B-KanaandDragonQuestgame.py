#https://codeforces.com/problemset/problem/1337/B

t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    if x <= m*10:
        print("YES")
    else:
        while n > 0:
            x = x // 2 + 10
            n -= 1
            if x <= 20:
                break
        if x <= m*10:
            print("YES")
        else:
            print("NO")
