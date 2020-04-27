#https://codeforces.com/contest/1342/problem/A

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if x == y == 0:
        print(0)
    else:
        output = 0
        if a*2 > b:
            output =  min(x, y)*b + abs(x-y)*a
        else:
            output = (x+y) * a
        print(output)
