#https://codeforces.com/problemset/problem/712/B

s = input()
if len(s) % 2 == 1:
    print(-1)
else:
    ans = 0
    l, r = sorted([s.count("L"), s.count("R")])
    u, d = sorted([s.count("U"), s.count("D")])
    if (l+r) % 2 == 0:
        ans += ((l+r) // 2 - l) + ((u+d) // 2 - u)
    else:
        ans += ((l+r+1) // 2 - l) + ((u+d-1) // 2 - u)
    print(ans)
