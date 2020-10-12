#https://codeforces.com/problemset/problem/1427/A

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
    if sum(a) == 0:
        print("NO")
    else:
        print("YES")
        print(*sorted(a, reverse=(True if total > 0 else False)))
