#https://codeforces.com/problemset/problem/688/A

n, d = map(int, input().split())
count = 0
best = 0
for _ in range(d):
    s = input()
    if "0" in s:
        count += 1
        best = max(best, count)
    else:
        count = 0
print(best)
