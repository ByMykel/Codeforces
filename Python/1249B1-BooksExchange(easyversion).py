#https://codeforces.com/contest/1249/problem/B1

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(str, input().split())
inl = lambda: list(map(int, input().split()))

q = ini()
for _ in range(q):
    n = ini()
    a = inl()
    ans = [0] * n
    for i in range(n):
        if ans[i] != 0:
            continue
        ok = []
        count = 1
        x = a[i] - 1
        while x != i:
            ok.append(x)
            x = a[x] - 1
            count += 1
        ans[i] = count
        for j in ok:
            ans[j] = count
    print(*ans)
