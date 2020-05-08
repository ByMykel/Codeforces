#https://codeforces.com/contest/1236/problem/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if b == 0:
        print(0)
    else:
        output = min(b, c//2)
        b -= output
        output += min(a, b//2)
        print(output * 3)
