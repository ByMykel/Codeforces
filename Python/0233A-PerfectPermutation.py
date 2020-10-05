#https://codeforces.com/problemset/problem/233/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
if n % 2:
    print(-1)
else:
    ans = []
    for i in range(1, n+1, 2):
        ans.append(i+1)
        ans.append(i)
    print(*ans)
