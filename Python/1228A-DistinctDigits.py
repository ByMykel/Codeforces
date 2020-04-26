#https://codeforces.com/problemset/problem/1228/A

l, r = map(int, input().split())
output = -1
for i in range(l, r+1):
    if len(set(str(i))) == len(str(i)):
        output = i
        break
print(output)
