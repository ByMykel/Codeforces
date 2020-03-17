#https://codeforces.com/problemset/problem/580/A

n = int(input())
a = list(map(int, input().split()))
solution = 1
count = 1
for i in range(n-1):
    if a[i] <= a[i+1]:
        count += 1
        if i == n-2 and count > solution:
            solution = count
    else:
        if count > solution:
            solution = count
        count = 1
print(solution)
