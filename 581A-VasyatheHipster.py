#https://codeforces.com/contest/581/problem/A

a, b = map(int, input().split())
print(min(a, b), int(abs(a - b) / 2))
