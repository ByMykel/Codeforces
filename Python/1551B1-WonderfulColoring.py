#https://codeforces.com/contest/1551/problem/B1

import sys

input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s="\n": print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    s = ins()
    count = dict()
    repeated, not_repeated = 0, 0
    for i in s:
        if i not in count:
            count[i] = 0
            not_repeated += 1
        if count[i] == 1:
            repeated += 1
            not_repeated -= 1
        count[i] += 1
    print(repeated + not_repeated // 2)
