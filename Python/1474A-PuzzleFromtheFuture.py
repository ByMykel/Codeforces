#https://codeforces.com/problemset/problem/1474/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n = ini()
    b = ins()
    ans = ""
    prev = -1
    for i in b:
        if i == "1":
            if prev != 2:
                ans += "1"
                prev = 2
            else:
                ans += "0"
                prev = 1
        else:
            if prev != 1:
                ans += "1"
                prev = 1
            else:
                ans += "0"
                prev = 0
    print(ans)
