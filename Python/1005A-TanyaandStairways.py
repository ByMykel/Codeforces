#https://codeforces.com/problemset/problem/1005/A

n = int(input())
a = list(map(int, input().split()))
output = []
count = 0
for i in range(n):
    if a[i] > count:
        count = a[i]
    else:
        output.append(count)
        count = 1
print(a.count(1))
print(*output, a[-1])
