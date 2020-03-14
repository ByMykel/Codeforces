#https://codeforces.com/problemset/problem/460/A

n, m = map(int, input().split())
solution, i = 0, 1
while True:
    n -= 1
    solution += 1
    if i % m == 0:
        n += 1
    if n == 0:
        break
    i += 1
print(solution)
