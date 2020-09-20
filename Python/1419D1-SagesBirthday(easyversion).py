#https://codeforces.com/problemset/problem/1419/D1

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = sorted(inl())
ans = []
while len(a) > 0:
    ans.append(a.pop())
    if len(a) == 0:
        break
    ans.append(a.pop(0))
print(n//2 if n % 2 else n//2 - 1)
print(*ans)
