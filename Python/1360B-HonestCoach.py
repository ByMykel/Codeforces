#https://codeforces.com/problemset/problem/1360/B

t = int(input())
for _ in range(t):
    n = int(input())
    s = sorted(list(map(int, input().split())))
    solution = 999
    for i in range(n-1):
        solution = min(solution, s[i+1] - s[i])
    print(solution)
