#https://codeforces.com/problemset/problem/118/A

s = input().lower()
for i in s:
    if i in "aoyeui":
        s = s.replace(i, "")
for i in s:
    print(f".{i}", end="")
