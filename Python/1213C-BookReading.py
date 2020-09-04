#https://codeforces.com/problemset/problem/1213/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, m = inm()
    first = []
    for i in range(1, 11):
        first.append(int(str(m*i)[-1]))
    ans = 0
    if n >= m * 10:
        ans += n // (m*10) * sum(first) + sum(first[:(n % (m*10) // m)])
    elif n >= m:
        ans += sum(first[:n//m])
    print(ans)
