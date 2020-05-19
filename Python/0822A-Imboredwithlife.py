#https://codeforces.com/problemset/problem/822/A

a, b = map(int, input().split())
output = 1
for i in range(2, min(a, b)+1):
    output *= i
print(output)
