#https://codeforces.com/problemset/problem/1144/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

N = 2 * 10**5 + 1
n = ini()
a = inl()
count = [0] * N
for i in a:
    count[i] += 1
if max(count) > 2:
    print("NO")
else:
    inc = []
    dec = []
    for i in range(N):
        if count[i] == 1:
            inc.append(i)
        elif count[i] == 2:
            inc.append(i)
            dec.insert(0, i)
    print("YES")
    print(len(inc))
    print(*inc)
    print(len(dec))
    print(*dec)
