#https://codeforces.com/problemset/problem/702/A

n = int(input())
a = list(map(int, input().split()))
output = 0
count = 0
prev = 0
for i in a:
    if i > prev:
        count += 1
    else:
        count = 1
    output = max(output, count)
    prev = i
print(output)
