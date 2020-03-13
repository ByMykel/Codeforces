#https://codeforces.com/contest/141/problem/A

g = input()
r = input()
p = input()
if sorted(g + r) == sorted(p):
    print("YES")
else:
    print("NO")
