#https://codeforces.com/problemset/problem/1140/A

n = int(input())
a = list(map(int, input().split()))
ans = 0
stop = 1
for i in range(n):
    stop = max(stop, a[i])
    if stop == i+1:
        ans += 1
print(ans)
