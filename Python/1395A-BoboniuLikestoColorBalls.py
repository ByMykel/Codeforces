#https://codeforces.com/problemset/problem/1395/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

ans = []
t = ini()
for _ in range(t):
    a = inl()
    even = 0
    for i in a:
        if i % 2 == 0:
            even += 1
    if even in [0, 3, 4]:
        ans.append("Yes")
    elif a[0] > 0 and a[1] > 0 and a[2] > 0 and even == 1:
        ans.append("Yes")
    else:
        ans.append("No")
print('\n'.join(map(str, ans)))
