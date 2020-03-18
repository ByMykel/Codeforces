#https://codeforces.com/problemset/problem/337/A

n, m = map(int, input().split())
f = sorted(list(map(int, input().split())))
suma = []
solution = 100000000
count, i, j = 0, 0, 0
while True:
    suma.append(f[i])
    count += 1
    if count == n:
        solution = min(solution, max(suma) - min(suma))
        suma = []
        i = j
        j += 1
        count = 0
    i += 1
    if i == m:
        break
print(solution)
