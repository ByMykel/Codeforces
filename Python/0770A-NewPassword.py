#https://codeforces.com/problemset/problem/770/A

n, k = map(int, input().split())
a = "abcdefghijklmnopqrstuvwxyz"
print((a[:k]*n)[:n])
