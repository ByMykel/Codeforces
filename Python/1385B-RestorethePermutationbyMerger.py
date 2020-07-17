#https://codeforces.com/contest/1385/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    output = []
    for i in a:
        if i in output:
            continue
        else:
            output.append(i)
    print(*output)
