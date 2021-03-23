#https://codeforces.com/contest/1501/problem/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
for _ in range(t):
    n = ini()
    a = inl()
    ans = [0] * n
    count = 0
    for i in range(n-1, -1, -1):
        count = max(count, a[i])
        if count > 0:
            ans[i] = 1
            count -= 1
    print(*ans)
