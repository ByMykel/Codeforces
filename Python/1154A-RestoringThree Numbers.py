#https://codeforces.com/problemset/problem/1154/A

x1, x2, x3, x4 = sorted(map(int, input().split()))
print(f"{x4 - x3} {x4 - x2} {x4 - x1}")
