#https://codeforces.com/problemset/problem/1419/D2

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = sorted(inl())
ans = []
count = 0
for i in range(n//2):
    ans.append(a[i + n//2])
    ans.append(a[i])
if n % 2:
    ans.append(a[-1])
for i in range(1, n-1):
    count += 1 if ans[i] < ans[i-1] and ans[i] < ans[i+1] else 0
print(count)
print(*ans)
