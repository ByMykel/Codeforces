#https://codeforces.com/problemset/problem/432/A

n, k = map(int, input().split())
times = list(map(int, input().split()))
times = [i for i in times if i < 5]
solution = 0
if len(times) >= 3:
    times = [i+k for i in times]
    times = [i for i in times if i <= 5]
    solution = len(times) // 3
print(solution)
