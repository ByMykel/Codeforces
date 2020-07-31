#https://codeforces.com/problemset/problem/1206/B

n = int(input())
a = list(map(int, input().split()))
ans = 0
neg = 0
zer = 0
for i in a:
    if i > 0:
        if i != 1:
            ans += i - 1
    elif i < 0:
        if i != -1:
            ans += abs(i + 1)
        neg += 1
    else:
        ans += 1
        zer += 1
if neg % 2 == 1 and zer == 0:
    print(ans + 2)
else:
    print(ans)
