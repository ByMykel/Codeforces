#https://codeforces.com/problemset/problem/716/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, c = inm()
a = inl()
prev = 10**9 + 1
count = 0
for i in a:
    if prev >= i:
        count += 1
    else:
        count = 1
    prev = i + c
print(count)
