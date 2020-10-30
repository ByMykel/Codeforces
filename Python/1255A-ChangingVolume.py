#https://codeforces.com/problemset/problem/1255/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    a, b = inm()
    diff = abs(a - b)
    ans = 0
    for i in [5, 2]:
        x = diff // i
        diff %= i
        ans += x
    print(ans + diff)
