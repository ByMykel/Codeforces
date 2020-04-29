#https://codeforces.com/contest/673/problem/A

n = int(input())
t = list(map(int, input().split()))
output = 0
prev = 0
for i in t:
    if i - prev > 15:
        output = prev + 15
        break
    else:
        output = i + 15
    if i == 90 or output > 90:
        output = 90
    prev = i
print(output)
