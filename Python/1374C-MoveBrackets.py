#https://codeforces.com/problemset/problem/1374/C

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count = 0
    output = 0
    for i in s:
        if i == ")":
            count -= 1
        else:
            count += 1
        output = min(output, count)
    print(abs(output))
