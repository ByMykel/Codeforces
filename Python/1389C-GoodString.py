#https://codeforces.com/contest/1389/problem/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

output = []
t = ini()
for _ in range(t):
    s = ins()
    ans = 0
    for i in range(10):
        for j in range(10):
            k = 1
            count = 0
            for n in s:
                if k == 1:
                    if n == str(i):
                        count += 1
                        k = -k
                else:
                    if n == str(j):
                        count += 1
                        k = -k
            if i == j:
                ans = max(ans, count)
            else:
                count += -1 if count % 2 else 0
                ans = max(ans, count)
    output.append(len(s) - ans)
out(output)
