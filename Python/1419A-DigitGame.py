#https://codeforces.com/problemset/problem/1419/A

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
    s = ins()
    if n % 2 == 0:
        ans = 1
        for i in range(1, n, 2):
            if int(s[i]) % 2 == 0:
                ans = 2
                break
    else:
        ans = 2
        for i in range(0, n, 2):
            if int(s[i]) % 2 != 0:
                ans = 1
                break
    print(ans)
