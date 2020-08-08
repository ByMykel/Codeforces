#https://codeforces.com/problemset/problem/1095/B

n = int(input())
a = sorted(list(map(int, input().split())))
print(min(max(a) - min(a[1:]), max(a[:-1]) - min(a)))
