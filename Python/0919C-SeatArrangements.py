#https://codeforces.com/problemset/problem/919/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, m, k = inm()
ans = 0
col = [0] * m
for _ in range(n):
    s = ins()
    count = 0
    for i in range(m):
        if s[i] == ".":
            count += 1
            col[i] += 1
            if count >= k:
                ans += 1
            if n == 1 or k == 1:
                continue
            if col[i] >= k:
                ans += 1
        else:
            count = 0
            col[i] = 0
print(ans)
