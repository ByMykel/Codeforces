#https://codeforces.com/problemset/problem/1244/B

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = n
    if "1" in s and s.index("1") < s[::-1].index("1"):
        s = s[::-1]
    for i in range(n):
        if s[i] == "1":
            tmp = i+1 + max(i, n-i-1) + 1
            ans = max(ans, tmp)
        else:
            continue
    print(ans)
