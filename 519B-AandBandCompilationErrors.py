#https://codeforces.com/problemset/problem/519/B

n = map(int, input().split())
a = sum(list(map(int, input().split())))
b = sum(list(map(int, input().split())))
c = sum(list(map(int, input().split())))
print(a - b)
print(b - c)
