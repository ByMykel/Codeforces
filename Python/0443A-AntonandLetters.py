#https://codeforces.com/problemset/problem/443/A

s = input()
if len(s) == 2:
    print(0)
else:
    s = s.replace("{", "").replace("}", "").split(", ")
    print(len(set(s)))
