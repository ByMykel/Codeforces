#https://codeforces.com/problemset/problem/43/A

t = int(input())
g = {}
for _ in range(t):
    s = input()
    if s not in g:
        g[s] = 1
    else:
        g[s] += 1
print(max(g, key=g.get))
