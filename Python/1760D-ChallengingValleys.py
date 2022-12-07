# https://codeforces.com/problemset/problem/1760/D

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
    b = []
    for i in a:
        if b != [] and i == b[-1]:
            continue
        b.append(i)
    count = 0
    x = len(b)
    if x == 1:
        print('YES')
        continue
    for i in range(x):
        if (i == 0 or b[i-1] > b[i]) and (i == x-1 or b[i+1] > b[i]):
            count += 1
    print('YES' if count == 1 else 'NO')
