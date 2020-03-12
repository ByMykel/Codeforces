#https://codeforces.com/problemset/problem/155/A

n = int(input())
num = list(map(int, input().split()))
mn, mx = num[0], num[0]
a = 0
for i in range(1, n):
    if mn > num[i]:
        mn = num[i]
        a += 1
    if mx < num[i]:
        mx = num[i]
        a += 1
print(a)
