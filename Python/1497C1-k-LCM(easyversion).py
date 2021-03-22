#https://codeforces.com/problemset/problem/1497/C1

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, k = inm()
    if n % 2:
        print(1, n//2, n//2)
    else:
        x = n//2
        if x % 2:
            print(2, x-1, x-1)
        else:
            print(x, x//2, x//2)
