#https://codeforces.com/problemset/problem/520/B

n, m = map(int, input().split())
times = 0
while n != m:
    if n > m or m % 2 != 0:
        m += 1
        times += 1
    else:
        if m % 2 == 0:
            m /= 2
            times += 1
print(times)
