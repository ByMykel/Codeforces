#https://codeforces.com/problemset/problem/1138/A

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    count = 0
    left = a[i]
    right = a[i + 1]
    for x in range(i+1):
        if left == right:
            break
        if i - x < 0 or i + x + 1 >= n:
            break
        if a[i - x] != left or a[i + x + 1] != right:
            break
        count += 2
    ans = max(ans, count)
print(ans)
