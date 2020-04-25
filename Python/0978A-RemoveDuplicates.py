#https://codeforces.com/problemset/problem/978/A

n = int(input())
a = list(map(int, input().split()))
b = set(a)
if len(b) == 1:
    print(1)
    print(a[0])
else:
    solution = []
    count = []
    for i in a[::-1]:
        if i in b and i not in count:
            solution.append(i)
            count.append(i)
        if len(count) == len(b):
            break
    print(len(b))
    print(*solution[::-1])
