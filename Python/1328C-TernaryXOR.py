#https://codeforces.com/problemset/problem/1328/C

t = int(input())
for i in range(t):
    n = int(input())
    x = input()
    a = "1"
    b = "1"
    for j in range(1, n):
        if x[j] == "2":
            a += "1"
            b += "1"
        elif x[j] == "0":
            a += "0"
            b += "0"
        else:
            a += "1" + "0" * (n-j-1)
            b += "0" + x[j+1:]
            break
    print(a)
    print(b)
