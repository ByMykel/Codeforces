#https://codeforces.com/problemset/problem/939/B

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans, j = n%a[0], 1
for i in range(1, k):
    tmp = n % a[i]
    if ans > tmp:
        ans = tmp
        j = i + 1
    if ans == 0:
        break
print(j, n//a[j-1])
