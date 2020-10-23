#https://codeforces.com/contest/1433/problem/A

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
    a = [1, 3, 6, 10]
    print((n % 10 - 1) * 10 + a[len(str(n)) - 1])
