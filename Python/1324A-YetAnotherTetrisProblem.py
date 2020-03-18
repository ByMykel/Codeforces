#https://codeforces.com/problemset/problem/1324/A

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == n:
        print("YES")
    elif odd == n:
        print("YES")
    else:
        print("NO")
