#https://codeforces.com/problemset/problem/1139/A

n = int(input())
s = input()
output = 0
for i in range(n):
    if int(s[i]) % 2 == 0:
        output += 1 + i
print(output)
