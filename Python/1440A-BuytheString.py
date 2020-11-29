#https://codeforces.com/problemset/problem/1440/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, c0, c1, h = inm()
    s = ins()
    count0 = s.count("0")
    count1 = s.count("1")
    print(min(count0 * c0 + count1 * c1, count0 * h + (count0 + count1) * c1, count1 * h + (count0 + count1) * c0))
