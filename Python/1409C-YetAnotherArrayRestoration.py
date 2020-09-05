#https://codeforces.com/problemset/problem/1409/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, x, y = inm()
    dif = y - x
    for i in range(1, dif+1):
        if dif % i != 0:
            continue
        count = n - 1
        start = y
        ok = False
        while count > 0 and start > 0:
            start -= i
            count -= 1
            if start == x:
                ok = True
        start += i if start <= 0 else 0
        if ok:
            break
    ans = []
    for j in range(n):
        ans.append(start + i*j)
    out(ans, " ")
