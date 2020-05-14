#https://codeforces.com/problemset/problem/22/A

n = int(input())
a = set(map(int, input().split()))
if len(a) == 1:
    print("NO")
else:
    print(sorted(a)[1])
