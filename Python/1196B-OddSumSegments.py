#https://codeforces.com/contest/1196/problem/B

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

t = ini()
for _ in range(t):
    n, k = inm()
    a = inl()
    odd = 0
    index = []
    for i in range(n):
        if a[i] % 2 != 0:
            odd += 1
            index.append(i+1)
    if odd < k:
        print("NO")
    elif odd == k or (odd - k + 1) % 2 != 0:
        print("YES")
        if k == 1:
            print(n)
        else:
            print(*index[:k-1], n)
    else:
        print("NO")
