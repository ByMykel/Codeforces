#https://codeforces.com/problemset/problem/746/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n = ini()
s = ins()
ans = ""
if n % 2:
    for i in range(n):
        if i % 2:
            ans = s[i] + ans
        else:
            ans += s[i]
else:
    for i in range(n):
        if i % 2:
            ans += s[i]
        else:
            ans = s[i] + ans
print(ans)
