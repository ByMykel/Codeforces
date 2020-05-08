#https://codeforces.com/problemset/problem/1294/A

t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())
    m = max(a, b, c)
    total = m-a + m-b + m-c
    if total > n:
        print("NO")
    elif (n-total) % 3 != 0:
        print("NO")
    else:
        print("YES")
