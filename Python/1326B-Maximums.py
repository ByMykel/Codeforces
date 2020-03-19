#https://codeforces.com/contest/1326/problem/B

n = int(input())
b = list(map(int, input().split()))
solution = [0] * n
x = 0
for i in range(n):
    solution[i] = b[i] + x
    if solution[i] > x:
        x = solution[i]
print(" ".join(map(str, solution)))
