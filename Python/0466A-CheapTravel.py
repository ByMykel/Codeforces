#https://codeforces.com/problemset/problem/466/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, m, a, b = inm()
print(min(n*a, (n+m-1) // m * b, n//m * b + n%m * a))
