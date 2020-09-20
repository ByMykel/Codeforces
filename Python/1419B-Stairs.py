#https://codeforces.com/contest/1419/problem/B

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
    ans = 0
    nice = 1
    while n > 0:
        x = nice * (nice+1) // 2
        if n - x >= 0:
            n -= x
            ans += 1
            nice = nice * 2 + 1
        else:
            break
    print(ans)
