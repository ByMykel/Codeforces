#https://codeforces.com/problemset/problem/337/A

n, m = map(int, input().split())
f = sorted(list(map(int, input().split())))
solution = 1000
for i in range(m-n+1):
    solution = min(solution, f[i+n-1] - f[i])
print(solution)
