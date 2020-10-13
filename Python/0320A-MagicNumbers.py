#https://codeforces.com/problemset/problem/320/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ins().replace("144", " ").replace("14", " ").replace("1", " ").replace(" ", "")
print("YES" if len(n) == 0 else "NO")
