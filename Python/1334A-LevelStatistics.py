#https://codeforces.com/contest/1334/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    lastp, lastc = 0, 0
    output = True
    for i in range(n):
        p ,c = map(int, input().split())
        if output == True:
            if p < c:
                output = False
                continue
            if p < lastp:
                output = False
                continue
            if c < lastc:
                output = False
                continue
            if p - lastp < c - lastc:
                output = False
                continue
            lastp, lastc = p, c
    print("YES" if output else "NO")
