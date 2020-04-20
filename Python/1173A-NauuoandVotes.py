#https://codeforces.com/problemset/problem/1173/A

x, y, z = map(int, input().split())
if x == y and z == 0:
    print("0")
elif x > y+z:
    print("+")
elif y > x+z:
    print("-")
else:
    print("?")
