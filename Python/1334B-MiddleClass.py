#https://codeforces.com/problemset/problem/1334/B

t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    if total / n >= x:
        print(n)
    else:
        for i in sorted(a):
            total -= i
            n -= 1
            if n == 0:
                output = 0
                break
            if total / n >= x:
                output = n
                break
        print(output)
