#https://codeforces.com/problemset/problem/1294/C

import sys
import math
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

t = ini()
ans = []
andsindex = [0] * t
for _ in range(t):
    n = ini()
    i = 2
    tmp = []
    while n >= i * i:
        if n % i == 0:
            tmp.append(i)
        if len(tmp) == 3:
            break
        i += 1
    if len(tmp) <= 1:
        ans.append("NO")
    elif len(tmp) >= 2:
        if len(tmp) == 3:
            if tmp[0] * tmp[1] * tmp[2] == n:
                ans.append("YES")
                andsindex[len(ans) - 1] = f"{tmp[0]} {tmp[1]} {tmp[2]}"
                continue
            y = (n / (tmp[0] * tmp[2])).is_integer()
            if y and n / (tmp[0] * tmp[2]) not in tmp:
                ans.append("YES")
                andsindex[len(ans) - 1] = f"{tmp[0]} {tmp[2]} {n // (tmp[0] * tmp[2])}"
                continue
        x = (n / (tmp[0] * tmp[1])).is_integer()
        if x and n / (tmp[0] * tmp[1]) not in tmp:
            ans.append("YES")
            andsindex[len(ans) - 1] = f"{tmp[0]} {tmp[1]} {n // (tmp[0] * tmp[1])}"
        else:
            ans.append("NO")
for i in range(t):
    print(ans[i])
    if ans[i] == "YES":
        print(andsindex[i])
