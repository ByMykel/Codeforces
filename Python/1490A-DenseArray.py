#https://codeforces.com/problemset/problem/1490/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
for i in range(t):
    n = ini()
    a = inl()
    ans = 0
    for i in range(n - 1):
        a_max = max(a[i], a[i + 1])
        a_min = min(a[i], a[i + 1])
        if a_max / a_min >= 2:
            tmp = a_min
            while tmp * 2 < a_max:
                tmp *= 2
                ans += 1
    print(ans)
