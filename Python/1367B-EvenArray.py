#https://codeforces.com/problemset/problem/1367/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    even, odd = 0, 0
    check = True
    for i in range(n):
        if check:
            if a[i] % 2 != 0:
                even += 1
            check = False
        else:
            if a[i] % 2 == 0:
                odd += 1
            check = True
    if even == odd == 0:
        print(0)
    elif even != odd:
        print(-1)
    else:
        print(even)
