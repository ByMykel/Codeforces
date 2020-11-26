#https://codeforces.com/problemset/problem/1454/C

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
    count = dict()
    prev = -1
    for i in a:
        if i not in count:
            count[i] = 1
        if prev != i:
            count[i] += 1
        prev = i
    ans = n
    for i in a:
        ans = min(ans, count[i] - (1 if a[0] == i else 0) - (1 if a[-1] == i else 0))
    print(ans)
