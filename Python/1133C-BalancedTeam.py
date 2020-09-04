#https://codeforces.com/problemset/problem/1133/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = sorted(inl())
i = 0
j = 0
ans = 1
while j < n:
    if i == j:
        j += 1
        continue
    if a[j] - a[i] <= 5:
        ans = max(ans, j - i + 1)
        j += 1
        continue
    else:
        i += 1
print(ans)
