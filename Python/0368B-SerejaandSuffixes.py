#https://codeforces.com/problemset/problem/368/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
checked = set()
ans = [0] * n
for i in range(n-1, -1, -1):
    checked.add(a[i])
    ans[i] = len(checked)
for _ in range(m):
    l = int(input())
    print(ans[l-1])
