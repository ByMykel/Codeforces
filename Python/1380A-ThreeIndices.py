#https://codeforces.com/problemset/problem/1380/A

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    output = False
    for i in range(1, n-1):
        if p[i] > p[i-1] and p[i] > p[i+1]:
            output = True
            print("YES")
            print(i, i+1, i+2)
            break
    if output == False:
        print("NO")
