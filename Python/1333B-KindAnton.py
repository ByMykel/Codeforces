#https://codeforces.com/problemset/problem/1333/B

import sys
input = sys.stdin.readline
ins = lambda: input()
ini = lambda: int(input())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

t = ini()
ans = []
for _ in range(t):
    n = ini()
    a = inl()
    b = inl()
    count = [0, 0]
    tmp = True
    for i in range(n):
        if a[i] > b[i] and count[1] == 0:
            tmp = False
            break
        elif a[i] < b[i] and count[0] == 0:
            tmp = False
            break
        if a[i] == 1:
            count[0] = 1
        if a[i] == -1:
            count[1] = 1
    ans.append("YES" if tmp else "NO")
print('\n'.join(ans))
