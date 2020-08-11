#https://codeforces.com/problemset/problem/1393/B

import sys
from collections import Counter
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(str, input().split())
inl = lambda: list(map(int, input().split()))
 
ans = []
n = ini()
a = inl()
q = ini()
count = dict(Counter(a))
r2 = 0
r4 = 0
for i in count.values():
    r2 += i // 2
    r4 += i // 4
for _ in range(q):
    p, s = inm()
    if p == "+":
        if int(s) in count:
            count[int(s)] += 1
        else:
            count[int(s)] = 1
        if count[int(s)] % 2 == 0:
            r2 += 1
        if count[int(s)] % 4 == 0:
            r4 += 1
    else:
        if count[int(s)] % 2 == 0:
            r2 -= 1
        if count[int(s)] % 4 == 0:
            r4 -= 1
        count[int(s)] -= 1
    ans.append("YES" if r2 >= 4 and r4 >= 1 else "NO")
print('\n'.join(ans))
