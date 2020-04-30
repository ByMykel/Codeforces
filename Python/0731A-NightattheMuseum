#https://codeforces.com/problemset/problem/731/A

letters = "abcdefghijklmnopqrstuvwxyz"
s = input()
prev = 0
output = 0
for i in s:
    actual = letters.index(i)
    rotations = abs(actual - prev)
    prev = actual
    if rotations > 13:
        output += 26 - rotations
    else:
        output += rotations
print(output)
