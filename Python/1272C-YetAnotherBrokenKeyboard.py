#https://codeforces.com/problemset/problem/1272/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n, k = inm()
a = ins()
c = list(ins().split())
ans = 0
count = 0
for i in a:
    if i in c:
        count += 1
    else:
        ans += count*(count+1) // 2
        count = 0
ans += count*(count+1) // 2
print(ans)
