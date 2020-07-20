#https://codeforces.com/problemset/problem/268/B

n = int(input())
add = 2
output = 1
for i in range(2, n+1):
    output += add
    add += i
print(output)
