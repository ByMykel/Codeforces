#https://codeforces.com/problemset/problem/263/A

for i in range(5):
    m = list(map(int, input().split()))
    if sum(m) > 0:
        if i == 2 and m.index(1) == 2:
            print(0)
        else:
            print(abs(2-i) + abs(2-m.index(1)))
