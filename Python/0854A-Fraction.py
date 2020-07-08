#https://codeforces.com/problemset/problem/854/A

n = int(input())
if n % 4 == 0:
    print(n//2 - 1, n//2 + 1)
elif n % 2 == 0:
    print(n//2 - 2, n//2 + 2)
else:
    print(n//2, n//2 + 1)
