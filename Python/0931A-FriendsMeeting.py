#https://codeforces.com/problemset/problem/931/A

a = int(input())
b = int(input())
d = abs(a - b)
n = d // 2
if d % 2 == 0:
    solution = n * ((n+1) / 2) * 2
else:
    solution = n * ((n+1) / 2) * 2 + n + 1
print(int(solution))
