#https://codeforces.com/problemset/problem/1536/A

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
    if min(a) < 0:
        print("NO")
    else:
        print("YES")
        print(101)
        print(*[i for i in range(0, 101)])
