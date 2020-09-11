#https://codeforces.com/problemset/problem/1311/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
alpha = {}
for i in range(26):
    alpha[chr(i + 97)] = 0
for _ in range(t):
    n, m = inm()
    s = ins()
    p = sorted(inl())
    prev = 0
    b = alpha.copy()
    for i in s:
        b[i] += 1
    for i in range(m):
        for j in range(prev, p[i]):
            b[s[j]] += (m - i)
        prev = p[i]
    print(*b.values())
