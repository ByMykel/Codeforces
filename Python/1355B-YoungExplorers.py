#https://codeforces.com/problemset/problem/1355/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

ans = []
t = ini()
for _ in range(t):
    n = ini()
    a = sorted(inl())
    tmp = 0
    count = 0
    for i in a:
        tmp += 1
        if tmp == i:
            count += 1
            tmp = 0
    ans.append(count)
out(ans)
