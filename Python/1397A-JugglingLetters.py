#https://codeforces.com/problemset/problem/1397/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

ans = []
t = ini()
for _ in range(t):
    n = ini()
    count = {}
    for _ in range(n):
        s = ins()
        for i in s:
            if i not in count:
                count[i] = 0
            count[i] += 1
    tmp = True
    for i, j in count.items():
        if j % n != 0:
            tmp = False
            break
    ans.append("YES" if tmp else "NO")
out(ans)
