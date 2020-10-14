#https://codeforces.com/problemset/problem/780/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
a = inl()
ans = 0
table = [0] * (10**5 + 1)
table_len = 0
for i in a:
    if not table[i]:
        table[i] = 1
        table_len += 1
    else:
        table_len -= 1
    ans = max(ans, table_len)
print(ans)
