#https://codeforces.com/problemset/problem/1208/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    a, b, n = inm()
    n = n % 3
    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        print(a ^ b)
