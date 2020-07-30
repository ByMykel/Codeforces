#https://codeforces.com/problemset/problem/888/B

n = int(input())
s = input()
x, y = 0, 0
for i in s:
    if i == "L":
        x -= 1
    if i == "R":
        x += 1
    if i == "U":
        y += 1
    if i == "D":
        y -= 1
print(n - (abs(x) + abs(y)))
