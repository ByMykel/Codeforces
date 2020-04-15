#https://codeforces.com/problemset/problem/1006/A

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] % 2 == 0:
        a[i] -= 1
print(*a)
