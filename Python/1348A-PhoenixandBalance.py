#https://codeforces.com/problemset/problem/1348/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
for _ in range(t):
    n = ini()
    print(2**n + sum(2**i for i in range(1, n//2)) - sum(2**i for i in range(n//2, n)))
