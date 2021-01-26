#https://codeforces.com/problemset/problem/1462/A

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
    ans = []
    for i in range(n//2):
        ans.append(a[i])
        ans.append(a[-i-1])
    print(*ans, a[n//2] if n % 2 else "")
