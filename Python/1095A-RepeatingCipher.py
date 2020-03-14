#https://codeforces.com/problemset/problem/1095/A

n = int(input())
s = input()
index, steps = 0, 1
while index < n:
    print(s[index], end="")
    steps += 1
    index += steps
