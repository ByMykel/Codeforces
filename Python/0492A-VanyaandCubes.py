#https://codeforces.com/problemset/problem/492/A

n = int(input())
solution, level, cube = 0, 1, 2
while cube <= n:
    n -= level
    if n >= 0:
        level += cube
        cube += 1
        solution += 1
    else:
        break
print(solution if solution > 0 else 1)
