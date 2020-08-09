#https://codeforces.com/problemset/problem/1304/B

n, m = map(int, input().split())
s = [0] * n
ans = []
pal = ""
for i in range(n):
    s[i] = input()
for i in range(n):
    if s[i][::-1] in s[i+1:]:
        ans.append(s[i])
    else:
        if pal == "" and s[i] == s[i][::-1]:
            pal = s[i]
print(2*m*len(ans) + len(pal))
print("".join(ans) + pal + "".join(map(lambda x: x[::-1], reversed(ans))))
