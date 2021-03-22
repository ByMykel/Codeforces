#https://codeforces.com/problemset/problem/1497/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n = ini()
    a = inl()
    b = [0] * 101
    for i in a:
        b[i] += 1
    start, end = [], []
    for i in range(101):
        if b[i] >= 1:
            start.append(i)
            if b[i] - 1 > 0:
                end.extend([i] * (b[i] - 1))
    print(*start, *end)
