#https://codeforces.com/problemset/problem/1176/B

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
    a = inl()
    count = [0, 0, 0]
    for i in a:
        count[i % 3] += 1
    count[0] += min(count[1], count[2])
    tmp = min(count[1], count[2])
    count[1] -= tmp
    count[2] -= tmp
    count[0] += count[1] // 3 + count[2] // 3
    ans.append(count[0])
out(ans)
