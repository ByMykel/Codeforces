#https://codeforces.com/problemset/problem/270/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

ans = []
t = ini()
for _ in range(t):
    n = ini()
    ans.append("YES" if (360 % (180 - n)) == 0 else "NO")
out(ans)
