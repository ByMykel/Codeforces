#https://codeforces.com/problemset/problem/1312/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    print(*a)
