#https://codeforces.com/problemset/problem/677/A

n, h = map(int, input().split())
a = list(map(int, input().split()))
road = 0
for i in a:
    if i > h:
        road += 2
    else:
        road +=1
print(road)
