#https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())
n = int((n+1) / 2)
print(2 * (k-n) if k > n else 2*k - 1)
