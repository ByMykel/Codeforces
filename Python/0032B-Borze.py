#https://codeforces.com/problemset/problem/32/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

s = ins()
print(s.replace("--", "2").replace("-.", "1").replace(".", "0"))
