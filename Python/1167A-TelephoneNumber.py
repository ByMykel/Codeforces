#https://codeforces.com/problemset/problem/1167/A

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if "8" not in s or n < 11:
        print("NO")
    else:
        if n - s.find("8") >= 11:
            print("YES")
        else:
            print("NO")
