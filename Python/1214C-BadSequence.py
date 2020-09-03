#https://codeforces.com/problemset/problem/1214/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
s = ins()
if n % 2 != 0:
    print("No")
else:
    count = 0
    ans = True
    for i in s:
        count += 1 if i == "(" else -1
        if count <= -2:
            ans = False
            break
    if count != 0:
        ans = False
    print("Yes" if ans else "No")
