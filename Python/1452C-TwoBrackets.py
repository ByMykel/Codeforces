#https://codeforces.com/contest/1452/problem/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
for _ in range(t):
    s = ins()
    ans = 0
    counta = 0
    countb = 0
    for i in s:
        if i == "(":
            counta += 1
            continue
        if i == ")":
            if counta > 0:
                ans += 1
                counta -= 1
            continue
        if i == "[":
            countb += 1
            continue
        if i == "]":
            if countb > 0:
                ans += 1
                countb -= 1
            continue
    print(ans)
