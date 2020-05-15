#https://codeforces.com/problemset/problem/1353/C

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
    else:
        output = 0
        for i in range(n//2, 0, -1):
            output += (n*4 - 4)*i
            n -= 2
        print(output)
