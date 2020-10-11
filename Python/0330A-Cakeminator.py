#https://codeforces.com/problemset/problem/330/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

r, c = inm()
col = [0] * c
count = 0
for _ in range(r):
    s = ins()
    for i in range(c):
        col[i] += 1 if s[i] == "." else -1
    if "S" not in s:
        count += c
if r == count // c:
    print(count)
else:
    print(count + col.count(r) * (r - count//c))
