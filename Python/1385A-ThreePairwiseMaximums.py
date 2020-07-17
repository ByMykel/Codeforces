#https://codeforces.com/contest/1385/problem/A

t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    if x == y == z:
        print("YES")
        print(x, x, x)
    elif x == y and x > z:
        print("YES")
        print(z, z, x)
    elif x == z and z > y:
        print("YES")
        print(y, y, x)
    elif y == z and y > x:
        print("YES")
        print(x, x, y)
    else:
        print("NO")
