#https://codeforces.com/problemset/problem/1146/A

s = input()
if s.count("a") > len(s) / 2:
    print(len(s))
else:
    print(s.count("a")*2 - 1)
