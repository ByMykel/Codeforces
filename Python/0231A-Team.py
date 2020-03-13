#https://codeforces.com/problemset/problem/231/A

n = int(input())
c = 0
for i in range(n):
    a = sum(map(int, input().split()))
    if a > 1:
        c += 1
print(c)
