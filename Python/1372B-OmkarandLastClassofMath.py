#https://codeforces.com/problemset/problem/1372/B

t = int(input())
for _ in range(t):
    n = int(input())
    k = n
    for i in range(2, 100000):
        if n % i == 0:
            k = i
            break
    if k == n:
        print(1, n-1)
    else:
        print(n//k, n - n//k)
