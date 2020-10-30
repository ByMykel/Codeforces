#https://codeforces.com/problemset/problem/1428/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    x1, y1, x2, y2 = inm()
    y = abs(y1 - y2)
    x = abs(x1 - x2)
    ans = x + y + (2 if x > 0 and y > 0 else 0)
    print(ans)
