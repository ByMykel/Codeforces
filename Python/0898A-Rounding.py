#https://codeforces.com/problemset/problem/898/A

n = int(input())
if n % 10 == 0:
    print(n)
else:
    last = n % 10
    if last <= 5:
        print(n - last)
    else:
        print(n + 10%last)
