#https://codeforces.com/problemset/problem/1092/B

n = int(input())
a = sorted(list(map(int, input().split())))
solution = 0
for i in range(0, n-1, 2):
    solution += a[i+1] - a[i]
print(solution)
