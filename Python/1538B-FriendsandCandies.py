#https://codeforces.com/problemset/problem/1538/B

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
    x = sum(a) / n
    if not x.is_integer():
        print(-1)
    else:
        ans = 0
        for i in a:
            if i > x:
                ans += 1
        print(ans)
