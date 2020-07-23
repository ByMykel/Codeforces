#https://codeforces.com/problemset/problem/1231/C

n, m = map(int, input().split())
a = [] 
ans = 0
out = True
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n-1, -1, -1):
    prev = a[i][m-1]
    if i < n-1 and prev >= a[i+1][m-1]:
        ans = -1
        break
    for j in range(m-2, -1, -1):
        if a[i][j] == 0:
            if i == n-1:
                a[i][j] = prev - 1
            else:
                a[i][j] = min(prev, a[i+1][j]) - 1
        if i == n-1:
            if a[i][j] >= prev:
                ans = -1
                out = False
        else:
            if a[i][j] >= prev or a[i][j] >= a[i+1][j]:
                ans = -1
                out = False
        prev = a[i][j]
    if out == False:
        break
    ans += sum(a[i])
print(ans)     
