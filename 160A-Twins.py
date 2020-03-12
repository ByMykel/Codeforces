#https://codeforces.com/problemset/problem/160/A

n = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse = True)
coins = 0
total = 0
for i in a:
    total += i
    coins += 1
    if total > sum(a) - total:
        break
print(coins)
