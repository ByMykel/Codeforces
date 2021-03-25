#https://codeforces.com/problemset/problem/1499/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
for _ in range(t):
    n, k1, k2 = inm()
    w, b, = inm()
    x = k1 + k2
    if x >= w * 2 and n*2 - x >= b * 2:
        print("YES")
    else:
        print("NO")
