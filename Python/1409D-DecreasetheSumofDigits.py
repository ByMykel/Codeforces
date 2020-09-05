#https://codeforces.com/problemset/problem/1409/D

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

def sum(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans

t = ini()
for _ in range(t):
    n, s = inm()
    ans = 0
    count = 1
    while True:
        if sum(n) <= s:
            break
        else:
            ans += (10 - n % 10) * count
            count *= 10
            n = (n + 10) // 10
    print(ans)
