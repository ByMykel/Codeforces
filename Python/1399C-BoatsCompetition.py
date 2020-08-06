#https://codeforces.com/contest/1399/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in a:
        b[i] += 1
    ans = 0
    for k in range(2, 2*n+1):
        count = 0
        for i in range(1, (k+1)//2 ):
            if k - i > n:
                continue
            count += min(b[i], b[k-i])
        if k % 2 == 0:
            count += b[k//2] // 2
        ans = max(ans, count)
    print(ans)
