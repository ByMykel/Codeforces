#https://codeforces.com/problemset/problem/1504/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    s = ins()
    if ('a' + s) != ('a' + s)[::-1]:
        print("YES")
        print('a' + s)
    elif (s + 'a') != (s + 'a')[::-1]:
        print("YES")
        print(s + 'a')
    else:
        print("NO")
