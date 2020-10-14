#https://codeforces.com/problemset/problem/1270/B

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
    ans = False
    for i in range(n-1):
        if abs(a[i] - a[i+1]) >= 2:
            print("YES")
            print(i+1, i+2)
            ans = True
            break
    if not ans:
        print("NO")
