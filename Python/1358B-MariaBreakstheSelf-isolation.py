#https://codeforces.com/problemset/problem/1358/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    output = 1
    b = 1
    for i in sorted(a):
        if b >= i:
            output = b + 1
        b += 1
    print(output)
