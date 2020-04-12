#https://codeforces.com/problemset/problem/1339/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    output = []
    right = n // 2
    left = right - 1
    while True:
        if right < n:
            output.append(a[right])
        else:
            break
        if left >= 0:
            output.append(a[left])
        else:
            break
        left -= 1
        right += 1
    print(*output)
