#https://codeforces.com/problemset/problem/946/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = inl()
first = 0
second = 0
for i in a:
    if i > 0:
        first += i
    else:
        second += i
print(first - second)
