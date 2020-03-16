#https://codeforces.com/problemset/problem/1223/A

for i in range(int(input())):
    q = int(input())
    if q == 2:
        print(2)
    elif q % 2 != 0:
        print(1)
    elif q % 2 == 0 and q > 2:
        print(0)
