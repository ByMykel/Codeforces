#https://codeforces.com/problemset/problem/1324/C

t = int(input())
for _ in range(t):
    s = input()
    a = s.split("R")
    print(len(max(a)) + 1)
