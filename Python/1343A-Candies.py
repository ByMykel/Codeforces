#https://codeforces.com/problemset/problem/1343/A

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, 30):
        if n % ((1 << i) - 1) == 0:
            print(n // ((1 << i) - 1))
            break
