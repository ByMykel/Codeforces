#https://codeforces.com/contest/1326/problem/B

n = int(input())
b = list(map(int, input().split()))
x = 0
for i in range(n):
    a = b[i] + x
    x = max(a, x)
    print(a, end=" ")
