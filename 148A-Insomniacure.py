#https://codeforces.com/problemset/problem/148/A

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
print(sum(1 for i in range(1, d+1) if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0))
