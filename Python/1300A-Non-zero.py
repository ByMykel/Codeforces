#https://codeforces.com/problemset/problem/1300/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) != 0 and 0 not in a:
        print(0)
    else:
        steps = a.count(0)
        if sum(a) + steps == 0:
            steps += 1
        print(steps)
