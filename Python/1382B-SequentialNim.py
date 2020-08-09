#https://codeforces.com/problemset/problem/1382/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i == 1:
            count += 1
        else:
            if count > 0:
                break
    if count == 0:
        print("First")
    elif count == n:
        print("First" if count % 2 else "Second")
    else:
        if a[0] == 1:
            print("Second" if count % 2 else "First")
        else:
            print("First")
