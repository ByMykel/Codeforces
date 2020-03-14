#https://codeforces.com/contest/732/problem/A

k, r = map(int, input().split())
shovel = 1
while True:
    if (k*shovel % 10) == 0 or (k*shovel % 10 - r) == 0:
        print(shovel)
        break
    else:
        shovel += 1
