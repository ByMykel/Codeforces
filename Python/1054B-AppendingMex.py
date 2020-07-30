#https://codeforces.com/problemset/problem/1054/B

n = int(input())
a = list(map(int, input().split()))
ans = -1
checked = {-1}
for i in range(n):
    if a[i] in checked:
        continue
    elif a[i]-1 in checked:
        checked.add(a[i])
        continue
    ans = i + 1
    break
print(ans)
