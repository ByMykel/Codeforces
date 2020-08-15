#https://codeforces.com/contest/1398/problem/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

ans = []
t = ini()
for _ in range(t):
    s = sorted(ins().split("0"), reverse=True)
    ans.append(sum([len(s[i]) for i in range(len(s)) if i % 2 == 0]))
print('\n'.join(map(str, ans)))
