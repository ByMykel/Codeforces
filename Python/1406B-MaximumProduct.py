#https://codeforces.com/problemset/problem/1406/B

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
    a = sorted(inl())
    if n == 5:
        ans = 1
        for i in range(5):
            ans *= a[i]
    else:
        pairs = []
        count = 2
        for i in range(0, n, 2):
            if count == 0 or a[i] >= 0 or a[i+1] >= 0:
                break
            pairs.append(a[i] * a[i+1])
            count -= 1
        ans = -(3 * 10**3)**5
        if len(pairs) == 2:
            ans = max(ans, pairs[0] * pairs[1] * a[-1])
        if len(pairs) >= 1:
            ans = max(ans, pairs[0] * a[-1] * a[-2] * a[-3])
        ans = max(ans, a[-1] * a[-2] * a[-3] * a[-4] * a[-5])
    print(ans)
