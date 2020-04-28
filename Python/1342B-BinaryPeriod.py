#https://codeforces.com/contest/1342/problem/B

n = int(input())
for _ in range(n):
    t = input()
    if len(set(t)) == 1:
        print(t)
    else:
        print("01" * len(t))
