#https://codeforces.com/problemset/problem/894/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

s = ins()
ans = 0
for i in range(len(s)):
    count = 0
    if s[i] != "Q":
        continue
    for j in range(i+1, len(s)):
        if s[j] == "A":
            count += 1
        if s[j] == "Q":
            ans += count
print(ans)
