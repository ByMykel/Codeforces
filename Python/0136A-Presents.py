#https://codeforces.com/problemset/problem/136/A

n = int(input())
numbers = list(map(int, input().split()))
solution = [0 for i in range(n)]
for i in range(n):
    solution[numbers[i]-1] = i+1
print(" ".join(str(i) for i in solution))
