#https://codeforces.com/contest/313/problem/B

s = input()
n = len(s)
a = [0] * n
m = int(input())
for i in range(1, n):
    a[i] = a[i-1] + (1 if s[i] == s[i-1] else 0)
for _ in range(m):
    l, r = map(int, input().split())
    ans = a[r-1] - a[l-1]
    print(ans)
