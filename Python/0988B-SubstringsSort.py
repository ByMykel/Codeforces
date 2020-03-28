#https://codeforces.com/contest/988/problem/B

n = int(input())
solution = [None] * n
for i in range(n):
    solution[i] = input()
solution = sorted(solution, key=len)
possible = True
for i in range(n-1):
    if solution[i] not in solution[i+1]:
        possible = False
        break
if possible:
    print("YES")
    print('\n'.join(solution))
else:
    print("NO")
