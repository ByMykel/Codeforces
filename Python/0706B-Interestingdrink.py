#https://codeforces.com/problemset/problem/706/B

import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    m = int(input())
    ans = bisect.bisect_right(a, m)
    print(ans)
