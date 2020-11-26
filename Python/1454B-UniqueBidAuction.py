#https://codeforces.com/problemset/problem/1454/B

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
    for i in a:
        if i not in count:
            count[i] = 0
        count[i] += 1
    b = sorted(filter(lambda x: x[1] == 1, count.items()), key=lambda x: x[0])
    if b:
        print(a.index(b[0][0]) + 1)
    else:
        print(-1)
