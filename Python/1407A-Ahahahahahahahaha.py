#https://codeforces.com/problemset/problem/1407/A

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
    ans = []
    for i in range(0, n, 2):
        if a[i] == a[i+1]:
            ans.append(a[i])
            ans.append(a[i])
        else:
            ans.append(0)
    print(len(ans))
    print(*ans)
