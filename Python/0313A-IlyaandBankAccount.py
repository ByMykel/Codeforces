#https://codeforces.com/problemset/problem/313/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n = ins()
print(max(int(n), int(n[:-1]), int(n[:-2] + n[-1])))
