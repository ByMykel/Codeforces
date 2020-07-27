#https://codeforces.com/problemset/problem/1165/B

n = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
prob = 1
for i in a:
    if prob <= i:
        ans += 1
        prob += 1
print(ans)
