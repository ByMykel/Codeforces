#https://codeforces.com/contest/1293/problem/B

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += 1/i
print(ans)
