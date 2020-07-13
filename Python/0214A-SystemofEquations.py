#https://codeforces.com/problemset/problem/214/A

n, m = map(int, input().split())
output = 0
for i in range(32):
    for j in range(32):
        if i**2 + j == n and i + j**2 == m:
            output += 1
        if i**2 + j > n or i + j**2 > m:
            continue
print(output)
