#https://codeforces.com/problemset/problem/1520/A

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
    s = ins()
    count = dict()
    last = ""
    ans = True
    for i in s:
        if i not in count:
            count[i] = 0
        else:
            if last != i:
                ans = False
                break
        count[i] += 1
        last = i
    print("YES" if ans else "NO")
