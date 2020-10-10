#https://codeforces.com/problemset/problem/513/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n1, n2, k1, k2 = inm()
print("First" if n1 > n2 else "Second")
