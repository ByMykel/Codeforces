#https://codeforces.com/problemset/problem/1257/C

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
    if n == 1 or len(a) == len(set(a)):
        print(-1)
    else:
        count = {}
        ans = n
        for i in range(n):
            if a[i] not in count:
                count[a[i]] = i
            else:
                ans = min(ans, i - count[a[i]])
                count[a[i]] = i
        print(ans + 1)
