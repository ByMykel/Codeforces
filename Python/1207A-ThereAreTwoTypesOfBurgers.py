#https://codeforces.com/problemset/problem/1207/A

t = int(input())
for i in range(t):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    if b < 2:
        print(0)
    else:
        b = b // 2
        beef = min(b, p) * h + min(b-min(b, p), f) * c
        chicken = min(b, f) * c + min(b-min(b, f), p) * h
        print(max(beef, chicken))
