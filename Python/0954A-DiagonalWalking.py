#https://codeforces.com/problemset/problem/954/A

n = int(input())
s = input()
output = 0
cont = False
for i in range(n-1):
    if cont:
        cont = False
        continue
    if s[i:i+2] in ["UR", "RU"]:
        output += 1
        cont = True
print(n - output)
