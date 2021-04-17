#https://codeforces.com/problemset/problem/701/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = sorted(enumerate(inl()), key=lambda x: x[1])
for i in range(n//2):
    print(a[i][0] + 1, a[-i-1][0] + 1)
