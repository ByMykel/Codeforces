#https://codeforces.com/problemset/problem/1141/B

n = int(input())
a = list(map(int ,input().split()))
ans = 0
count = 0
for i in a+a:
    if i == 1:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
print(ans)
