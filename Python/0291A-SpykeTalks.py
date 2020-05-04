#https://codeforces.com/contest/291/problem/A

n = int(input())
id = sorted(list(map(int, input().split())))
prev = -1
count = 1
output = 0
for i in id:
    if i == 0:
        continue
    if prev == i:
        count += 1
    else:
        count = 1
    if count == 2:
        output += 1
    elif count >= 3:
        output = -1
        break
    prev = i
print(output)
