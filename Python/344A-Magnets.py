#https://codeforces.com/problemset/problem/344/A

n = int(input())
last = int(input())
c = 1
for i in range(1, n):
    nl = int(input())
    if last != nl:
        c += 1
    last = nl
print(c)
