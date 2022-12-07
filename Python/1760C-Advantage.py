# https://codeforces.com/contest/1760/problem/C

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
    l = inl()
    x = sorted(l)
    ans = [i - x[-1] if i != x[-1] else i - x[-2] for i in l]
    print(*ans)
