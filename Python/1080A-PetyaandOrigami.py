#https://codeforces.com/problemset/problem/1080/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
ceil = lambda a, b: (a + b - 1) // b

n, k = inm()
print(ceil(n*2, k) + ceil(n*5, k) + ceil(n*8, k))
