#https://codeforces.com/problemset/problem/1335/B

alphabet  = "abcdefghijklmnopqrstuvwxyz"
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    print((alphabet[:b] * n)[:n])
