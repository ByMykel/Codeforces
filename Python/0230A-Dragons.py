#https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
xnew = [x for x, y in sorted(zip(x, y))]
ynew = [x for y, x in sorted(zip(x, y))]
for i in range(n):
    if s > xnew[i]:
        s += ynew[i]
        solution = "YES"
    else:
        solution = "NO"
        break
print(solution)
