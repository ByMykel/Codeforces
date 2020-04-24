#https://codeforces.com/problemset/problem/1296/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) % 2 != 0:
        print("YES")
    elif n == 1:
        print("NO")
    else:
        odd = even = 0
        solution = False
        for i in a:
            if i % 2 != 0:
                odd += 1
            else:
                even += 1
            if odd >= 1 and even >= 1:
                solution = True
                break
        if solution:
            print("YES")
        else:
            print("NO")
