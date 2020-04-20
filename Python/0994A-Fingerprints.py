#https://codeforces.com/problemset/problem/994/A

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
output = []
for i in x:
    if i in y:
        output.append(i)
print(*output)
