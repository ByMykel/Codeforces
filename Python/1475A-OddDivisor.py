#https://codeforces.com/problemset/problem/1475/A

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
    ans = False
    while n > 1:
        if n % 2:
            ans = True
            break
        n //= 2
    print("YES" if ans else "NO")
