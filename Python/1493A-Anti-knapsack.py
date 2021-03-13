#https://codeforces.com/problemset/problem/1493/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, k = inm()
    a = [i for i in range((k + 1) // 2, n + 1) if i != k]
    print(len(a))
    print(*a)
