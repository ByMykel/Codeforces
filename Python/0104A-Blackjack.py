#https://codeforces.com/problemset/problem/104/A

n = int(input()) - 10
if n == 1 or n == 11:
    print(4)
elif n > 1 and n < 10:
    print(4)
elif n == 10:
    print(15)
else:
    print(0)
