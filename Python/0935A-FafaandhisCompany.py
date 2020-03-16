#https://codeforces.com/problemset/problem/935/A

n = int(input())
solution = 1
for i in range(2, n):
    if (n-i)/i % 1 == 0:
        solution += 1
print(solution)
