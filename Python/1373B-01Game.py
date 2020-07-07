#https://codeforces.com/problemset/problem/1373/B

t = int(input())
for _ in range(t):
    s = input()
    n = min(s.count("1"), s.count("0"))
    if n == 0:
        print("NET")
    elif n % 2 == 0:
        print("NET")
    else:
        print("DA")
