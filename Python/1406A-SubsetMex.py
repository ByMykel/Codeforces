#https://codeforces.com/problemset/problem/1406/A

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
    first = second = -1
    for i in range(101):
        if a.count(i) > 1:
            continue
        if a.count(i) == 1 and first == -1:
            first = i
            continue
        if a.count(i) == 0:
            first = i if first == -1 else first
            second = i
            break
    print(first+second)
