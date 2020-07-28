#https://codeforces.com/problemset/problem/1136/B

n, k = map(int, input().split())
print(3*n + min(n-k, k-1))
