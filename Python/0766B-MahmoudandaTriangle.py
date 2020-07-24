#https://codeforces.com/problemset/problem/766/B

n = int(input())
a = sorted(list(map(int, input().split())))
ans = False
for i in range(n-2):
    if a[i] + a[i+1] > a[i+2]:
        ans = True
print("YES" if ans else "NO")
