#https://codeforces.com/contest/1324/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    checked = []
    ans = False
    for i in range(n):
        if a[i] not in checked:
            if a[i+2:].count(a[i]) > 0:
                ans = True
                break
            else:
                checked.append(a[i])
    print("YES" if ans else "NO")
