#https://codeforces.com/problemset/problem/1020/B

n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    ok = [0] * n
    k = i
    while ok[k] == 0:
        ok[k] = 1
        k = a[k] - 1
    ans.append(k + 1)
print(*ans)
