#https://codeforces.com/problemset/problem/467/A

n = int(input())
c = 0
for i in range(n):
    p, q = map(int, input().split())
    if p+2 <= q:
        c +=1
print(c)
