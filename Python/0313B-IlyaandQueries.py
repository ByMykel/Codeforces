#https://codeforces.com/problemset/problem/313/B

s = input()
n = len(s)
a = [0] * n
m = int(input())
for i in range(1, n):
    a[i] = 1 if s[i-1] == s[i] else 0
for _ in range(m):
    l, r = map(int, input().split())
    ans = sum(a[l:r])
    print(ans)
