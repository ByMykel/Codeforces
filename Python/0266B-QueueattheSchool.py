#https://codeforces.com/problemset/problem/266/B

n, t = map(int, input().split())
queue = input()
for i in range(t):
    queue = queue.replace("BG", "GB")
print(queue)