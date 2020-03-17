#https://codeforces.com/problemset/problem/490/A

n = int(input())
t = list(map(int, input().split()))
p, m, e = t.count(1), t.count(2), t.count(3)
teams = min(p, m, e)
p, m, e = [], [], []
for index, i in enumerate(t):
    if i == 1 and len(p) < teams:
        p.append(str(index+1))
    elif i == 2 and len(m) < teams:
        m.append(str(index+1))
    elif i == 3 and len(e) < teams:
        e.append(str(index+1))
    elif len(p+m+e) == teams*3:
        break
print(teams)
for i in range(teams):
    print(p[i], m[i], e[i])
