#https://codeforces.com/problemset/problem/451/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

n, m = inm()
if min(n, m) % 2 == 0:
    print("Malvika")
else:
    print("Akshat")
