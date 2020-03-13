#https://codeforces.com/problemset/problem/69/A

n = int(input())
x, y, z = 0, 0, 0
for i in range(n):
    c = list(map(int, input().split()))
    x += c[0]
    y += c[1]
    z += c[2]
print("YES" if abs(x)+abs(y)+abs(z) == 0 else "NO")
