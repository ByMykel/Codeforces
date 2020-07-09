#https://codeforces.com/problemset/problem/680/A

t = sorted(list(map(int, input().split())))
if len(set(t)) == 5:
    print(sum(t))
else:
    prev = 0
    total = 0
    count = 0
    output = 0
    for i in t:
        if prev != i:
            count = 0
            total = 0
        if count != 3:
            total += i
            count += 1
        if count >= 2:
            output = max(total, output)
        prev = i
    print(sum(t) - output)
