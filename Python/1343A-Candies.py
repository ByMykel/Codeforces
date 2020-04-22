#https://codeforces.com/problemset/problem/1343/A

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, 30):
        outout = n / (2**i - 1)
        if outout % 1 == 0:
            print(int(outout))
            break
