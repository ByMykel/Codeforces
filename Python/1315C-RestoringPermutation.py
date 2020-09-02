#https://codeforces.com/problemset/problem/1315/C

import sys
import bisect
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

t = ini()
for _ in range(t):
    n = ini()
    b = inl()
    a = [i for i in range(1, n*2+1) if i not in b]
    out = True
    for index, number in enumerate(sorted(b)):
        if number > a[index]:
            out = False
            print(-1)
            break
    if not out:
        continue
    ans = []
    for i in b:
        x = bisect.bisect_right(a, i)
        ans.append(i)
        ans.append(a[x])
        a.pop(x)
    print(*ans)
