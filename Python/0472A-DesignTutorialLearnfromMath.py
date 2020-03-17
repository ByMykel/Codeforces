#https://codeforces.com/problemset/problem/472/A

n = int(input())
if n % 2 == 0:
    if n//2 % 2 == 0:
        print(n//2, n//2)
    else:
        print(4, n-4)
else:
    print(9, n-9)
