#https://codeforces.com/problemset/problem/680/B

a, n = map(int, input().split())
t = list(map(int, input().split()))
i, j = n-2, n
ans = 1 if t[n-1] == 1 else 0
while i >= 0 or j < a:
    if i >=0 and j < a:
        if t[i] == t[j] == 1:
            ans += 2
    else:
        if i < 0 and t[j] == 1:
            ans += 1
        elif j >= a and t[i] == 1:
            ans += 1
    i -= 1
    j += 1
print(ans)
