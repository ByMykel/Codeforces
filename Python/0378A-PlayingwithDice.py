#https://codeforces.com/problemset/problem/378/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

a, b = inm()
ans = [0, 0, 0]
for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        ans[0] += 1
    elif abs(a - i) > abs(b - i):
        ans[2] += 1
    else:
        ans[1] += 1
print(*ans)
