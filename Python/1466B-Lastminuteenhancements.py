#https://codeforces.com/problemset/problem/1466/B

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
    a = sorted(inl())
    b = [0] * (2 * n + 2)
    ans = 0
    for i in a:
        if b[i] == 0:
            ans += 1
            b[i] = 1
        else:
            if b[i + 1] == 0:
                ans += 1
                b[i + 1] = 1
    print(ans)
