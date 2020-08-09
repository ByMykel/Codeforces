#https://codeforces.com/problemset/problem/1345/B

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    while n >= 2:
        count = 0
        tmp = 0
        i = 1
        while count < n:
            tmp += i * 2 + i - 1
            if tmp <= n:
                count = tmp
            else:
                break
            i += 1
        n -= count
        ans += 1
    print(ans)
