#https://codeforces.com/problemset/problem/1372/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sorted(a) == a:
        print(0)
    else:
        output = 1
        count = 0
        for i in range(n):
            if a[i] != i+1:
                if count == 2:
                    output = 2
                    break
                count = 1
            else:
                if count == 1:
                    count = 2
        print(output)
