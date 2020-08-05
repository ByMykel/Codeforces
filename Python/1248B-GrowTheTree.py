#https://codeforces.com/problemset/problem/1248/B

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
k = n//2 + 1 if n % 2 else n // 2
ans = sum(a[:k]) ** 2 + sum(a[k:]) ** 2
print(ans)
