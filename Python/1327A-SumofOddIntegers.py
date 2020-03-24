#https://codeforces.com/problemset/problem/1327/A

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    n = n - k**2
    if n < 0:
        print("NO")
    elif n % 2 == 0:
        print("YES")
    else:
        print("NO")
