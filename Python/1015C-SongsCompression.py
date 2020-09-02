#https://codeforces.com/problemset/problem/1015/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n, m = inm()
a = 0
b = []
for _ in range(n):
    i, j = inm()
    a += i
    b.append(i-j)
if a <= m:
    print(0)
else:
    if a - m > sum(b):
        print(-1)
    else:
        b = sorted(b, reverse=True)
        count = a - m
        ans = 0
        for i in b:
            count -= i
            ans += 1
            if count <= 0:
                break
        print(ans)
