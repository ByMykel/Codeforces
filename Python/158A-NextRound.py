#https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
if n < k:
    print(0)
else:
    c = 0
    a = list(map(int, input().split()))
    for number in a:
        if a[k-1] < 0:
            break
        if number >= a[k-1] and number != 0:
            c += 1
    print(c)
