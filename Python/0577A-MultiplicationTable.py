#https://codeforces.com/problemset/problem/577/A

n, x = map(int, input().split())
occurs = 0
for i in range(1, n+1):
    if x % i == 0 and x / i <= n:
        occurs += 1
print(occurs)
