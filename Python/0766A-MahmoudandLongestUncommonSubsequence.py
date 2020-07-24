#https://codeforces.com/problemset/problem/766/A

a = input()
b = input()
if a == b:
    print(-1)
else:
    print(max(len(a), len(b)))
