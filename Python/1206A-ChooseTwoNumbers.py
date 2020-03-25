#https://codeforces.com/problemset/problem/1206/A

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))
print(a[n-1], b[m-1])
