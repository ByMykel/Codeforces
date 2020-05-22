#https://codeforces.com/problemset/problem/381/A

n = int(input())
a = list(map(int, input().split()))
s = 0
d = 0
while len(a) > 0:
    if len(a) == 1:
        s += a.pop()
        break
    elif a[0] > a[len(a)-1]:
        s += a.pop(0)
    else:
        s += a.pop()
    if a[0] > a[len(a)-1]:
        d += a.pop(0)
    else:
        d += a.pop()
print(s, d)
