#https://codeforces.com/problemset/problem/1513/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
for i in range(t):
    n, k = inm()
    if (n + 1) // 2 - 1 < k:
        print(-1)
    else:
        ans = [i for i in range(1, n+1)]
        for i in range(1, n-1, 2):
            if k == 0:
                break
            ans[i], ans[i+1] = ans[i+1], ans[i]
            k -= 1
        print(*ans)
