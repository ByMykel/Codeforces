#https://codeforces.com/problemset/problem/1360/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    even = 0
    odd = 0
    close = 0
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1
        if i == n-1:
            break
        if a[i] - a[i+1] == -1:
            close += 1 
    if even % 2 == 0:
        print("YES")
    elif even == 0 or odd == 0:
        print("YES")
    elif close == 0:
        print("NO")
    else:
        print("YES")
