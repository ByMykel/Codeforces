#https://codeforces.com/problemset/problem/1323/A

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] % 2 == 0:
            print(1)
            print(1)
        else:
            print(-1)
    else:
        odd = [] * 2
        even = False
        for i in range(n):
            if a[i] % 2 == 0:
                print(1)
                print(i + 1)
                even = True
                break
            else:
                if len(odd) != 2:
                    if a[i] not in odd:
                        odd.append(i+1)
                    elif a[i] in odd and i == n-1:
                        odd.append(i+1)
        if even == False:
            print(2)
            print(odd[0], odd[1])
