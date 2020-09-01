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
        ans = s[i] + ans if i % 2 else ans + s[i]
else:
    for i in range(n):
        ans = ans + s[i] if i % 2 else s[i] + ans
print(ans)
