#https://codeforces.com/problemset/problem/1106/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = sorted(inl())
ans = 0
for i in range(n//2):
    ans += (a[i] + a[-i-1])**2
print(ans)
