#https://codeforces.com/contest/567/problem/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = inl()
a = list(map(lambda x: x - a[0], a))
for i in range(n):
    if i == 0:
        print(a[1], a[n-1])
    elif i == n - 1:
        print(a[n-1] - a[n-2], a[n-1])
    else:
        print(min(a[i] - a[i-1], a[i+1] - a[i]), max(a[i] - a[0], a[n-1] - a[i]))
