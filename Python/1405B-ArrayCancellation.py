#https://codeforces.com/problemset/problem/1405/B

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
    ans = 0
    count = 0
    for i in a[::-1]:
        if i < 0:
            count += i
        else:
            ans += max(0, i+count)
            count = 0 if i+count >= 0 else i+count 
    print(ans)
