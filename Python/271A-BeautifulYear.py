#https://codeforces.com/problemset/problem/271/A

n = int(input()) + 1
while True:
    if len(set(i for i in str(n))) != 4:
        n += 1
    else:
        print(n)
        break
