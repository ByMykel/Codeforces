#https://codeforces.com/problemset/problem/1371/A

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n//2 + 1)
