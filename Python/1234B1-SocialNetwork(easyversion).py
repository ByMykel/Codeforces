#https://codeforces.com/problemset/problem/1234/B1

n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in a:
    if i not in ans:
        if len(ans) < k:
            ans.append(i)
        else:
            ans.pop(0)
            ans.append(i)
print(len(ans))
print(*reversed(ans)) 
