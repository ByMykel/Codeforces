#https://codeforces.com/problemset/problem/1107/B

n = int(input())
for _ in range(n):
    k, x = map(int, input().split())
    print(9 * (k-1) + x)
