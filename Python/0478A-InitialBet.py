#https://codeforces.com/problemset/problem/478/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

a = sum(inl())
n = a / 5
print(int(n) if n.is_integer() and n != 0 else -1)
