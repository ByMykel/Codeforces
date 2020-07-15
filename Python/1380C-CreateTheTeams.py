#https://codeforces.com/contest/1380/problem/C

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    output = 0
    count = 1
    for i in a:
        if i * count >= x:
            output += 1
            count = 0
        count += 1
    print(output)
