#https://codeforces.com/contest/1077/problem/A

t = int(input())
for i in range(t):
    a, b, k = map(int, input().split())
    if k % 2 == 0:
        print(a * (k//2) - b * (k//2))
    else:
        print(a * (k//2 + 1) - b * (k - (k//2 + 1)))
