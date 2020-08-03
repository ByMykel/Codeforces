#https://codeforces.com/problemset/problem/1351/B

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a2, b2 = map(int, input().split())
    if a in [a2, b2] and a2+b2-a+b == a:
        print("Yes")
    elif b in [a2, b2] and a2+b2-b+a == b:
        print("Yes")
    else:
        print("No")
