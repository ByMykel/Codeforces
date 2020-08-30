#https://codeforces.com/problemset/problem/580/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))
 
n, m = inm()
c = inl()
graph = {}
for i in range(n-1):
    a, b = inm()
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)
stack = [(1, 0, 0)]
ans = 0
while len(stack) != 0:
    x, count, prev = stack.pop()
    if c[x-1] == 1:
        count += 1
    else:
        count = 0
    if count > m:
        continue
    if len(graph[x]) == 1 and x != 1:
        ans += 1
        continue
    for i in graph[x]:
        if i == prev:
            continue
        stack.append((i, count, x))
print(ans)
