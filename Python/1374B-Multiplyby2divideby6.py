#https://codeforces.com/problemset/problem/1374/B

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    while n > 1:
        if n % 6 == 0:
            n /= 6
        else:
            n *= 2
            if n % 3 != 0:
                ans = -1
                break
        ans += 1
    print(ans)
