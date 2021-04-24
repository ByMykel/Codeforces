#https://codeforces.com/problemset/problem/1509/A

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
    even = []
    odd = []
    for i in a:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    print(*even, *odd)
