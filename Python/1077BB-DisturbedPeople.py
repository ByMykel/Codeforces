#https://codeforces.com/contest/1077/problem/B

n = int(input())
a = list(map(int, input().split()))
solution = 0
for i in range(1, n-1):
    if a[i] == 0:
        if a[i-1] == 1 and a[i+1] == 1:
            a[i+1] = 0
            solution += 1
print(solution)
