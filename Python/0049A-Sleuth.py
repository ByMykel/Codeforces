#https://codeforces.com/problemset/problem/49/A

s = input().replace(" ", "")
if s[-2].lower() in "aeiouy":
    print("YES")
else:
    print("NO")
