#https://codeforces.com/problemset/problem/1454/A

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
    ans = [i for i in range(n, 0, -1)]
    if n % 2:
        ans[-1], ans[n//2] = ans[n//2], ans[-1]
    print(*ans)
