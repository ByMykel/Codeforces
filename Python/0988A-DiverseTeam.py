#https://codeforces.com/contest/988/problem/A

n, k = map(int, input().split())
a = list(map(int, input().split()))
if len(set(a)) < k:
    print("NO")
else:
    team = list(set(a))
    solution = [None] * k 
    for i in range(k):
        solution[i] = a.index(team[i]) + 1
    print(f"YES\n{' '.join(map(str, solution))}")
