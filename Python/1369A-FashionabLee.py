#https://codeforces.com/problemset/problem/1369/A

t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if n % 4 == 0 else "NO")
