#https://codeforces.com/problemset/problem/1375/B

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    output = True
    for i in range(n):
        if output == False:
            break
        for j in range(m):
            a = 0
            if i > 0:
                a += 1
            if j > 0:
                a += 1
            if i < n - 1:
                a += 1
            if j < m -1:
                a += 1
            if a < grid[i][j]:
                output = False
                break
            grid[i][j] = a
    if output:
        print("YES")
        for i in grid:
            print(*i)
    else:
        print("NO")
