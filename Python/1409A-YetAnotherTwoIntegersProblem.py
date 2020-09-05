#https://codeforces.com/problemset/problem/1409/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    a, b = inm()
    tmp = abs(a - b)
    if tmp == 0:
        print(0)
    else:
        print((tmp + 9) // 10)
