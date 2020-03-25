#https://codeforces.com/problemset/problem/1003/A

n = int(input())
a = sorted(list(map(int, input().split())))
solution = 1
count = 1
last = a[0]
for i in a[1:]:
    if last == i:
        count += 1
        solution = max(solution, count)
    else:
        count = 1
    last = i
print(solution)
