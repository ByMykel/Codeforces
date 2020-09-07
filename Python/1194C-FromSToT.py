#https://codeforces.com/problemset/problem/1194/C

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
    t = ins()
    p = list(ins())
    j = 0
    ans = False
    for i in range(len(t)):
        if j < len(s):
            if t[i] != s[j] and t[i] not in p:
                break
            elif t[i] == s[j]:
                j += 1
            elif t[i] in p:
                p.remove(t[i])
            else:
                break
        else:
            if t[i] not in p:
                break
            else:
                p.remove(t[i])
        if i == len(t) - 1 and j == len(s):
            ans = True
    print("YES" if ans else "NO")
