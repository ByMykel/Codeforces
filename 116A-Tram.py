#https://codeforces.com/contest/116/problem/A

n = int(input())
capacity = 0
s = 0
for i in range(n):
    a, b = map(int, input().split())
    capacity  = s if s > capacity else capacity 
    s += b - a
print(capacity)
