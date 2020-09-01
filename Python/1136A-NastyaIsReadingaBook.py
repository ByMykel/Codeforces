#https://codeforces.com/problemset/problem/1136/A

import sys
import bisect
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n = ini()
chap = []
for _ in range(n):
    a, b = inm()
    chap.append(a)
    chap.append(b)
index = ini()
x = bisect.bisect_left(chap , index)
print(n - x // 2)
