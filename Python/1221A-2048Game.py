#https://codeforces.com/contest/1221/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    if 2048 in a:
        print("YES")
    else:
        count = 0
        out = False
        for i in a:
            if i < 2048:
                count += i
            if count >= 2048:
                out = True
                break
        print("YES" if out else "NO")
