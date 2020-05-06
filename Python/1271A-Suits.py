#https://codeforces.com/problemset/problem/1271/A

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if e >= f:
    output = min(a, d)*e + min(b, c, d-min(a, d))*f
elif e < f:
    output = min(b, c, d)*f + min(a, d-min(b, c, d))*e
print(output)
