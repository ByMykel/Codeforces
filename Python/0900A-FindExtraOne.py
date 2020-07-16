#https://codeforces.com/problemset/problem/900/A

n = int(input())
output = True
l, r = 0, 0
for _ in range(n):
    x, y = map(int, input().split())
    if x < 0:
        l += 1
    else:
        r += 1
    if l >= 2 and r >= 2:
        output = False
        break
print("Yes" if output else "No")
