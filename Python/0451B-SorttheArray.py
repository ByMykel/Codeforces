#https://codeforces.com/problemset/problem/451/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

n = ini()
a = inl()
if a == sorted(a):
    print("yes")
    print(1, 1)
elif a == sorted(a, reverse=True):
    print("yes")
    print(1, n)
else:
    left = 0
    right = 0
    b = sorted(a)
    for i in range(n):
        if a[i] != b[i]:
            left = i
            break
    for i in range(n-1, -1, -1):
        if a[i] != b[i]:
            right = i
            break
    c = a[:left], list(reversed(a[left:right + 1])), a[right+1:]
    d = b[:left], b[left:right + 1], b[right+1:]
    if c == d:
        print("yes")
        print(left+1, right+1)
    else:
        print("no")
