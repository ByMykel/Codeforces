#https://codeforces.com/problemset/problem/1353/B

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n == k:
        print(sum(sorted(a+b)[-n:]))
    else:
        a = sorted(a)
        b = sorted(b)
        i = 0
        while min(a) < max(b) and k > 0:
            a[i], b[n-i-1] = b[n-i-1], a[i]
            k -= 1
            i += 1
        print(sum(a))
