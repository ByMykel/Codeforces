#https://codeforces.com/problemset/problem/58/A

s = input()
l = "hello"
j = 0
for i in s:
    if j == 5:
        break
    elif i == l[j]:
        j += 1
print("YES" if j == 5 else "NO")
