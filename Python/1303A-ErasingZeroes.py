#https://codeforces.com/problemset/problem/1303/A

t = int(input())
for i in range(t):
    s = input()
    if s.count("1") < 2:
        print(0)
    else:
        n = len(s)
        start = s.find("1")
        stop = n - s[::-1].find("1") - 1
        print(s[start:stop].count("0"))
