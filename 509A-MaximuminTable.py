#https://codeforces.com/contest/509/problem/A

n = int(input())
table = [[1] * n for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        table[i][j] = table[i-1][j] + table[i][j-1]
print(table[n-1][n-1])
