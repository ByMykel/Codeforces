#https://codeforces.com/problemset/problem/598/A

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
    ans = n * (n+1) // 2
    for i in range(30):
        if 2**i <= n:
            ans -= (2**i * 2)
        else:
            break
    print(ans)
