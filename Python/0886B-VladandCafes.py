#https://codeforces.com/problemset/problem/886/B

n = int(input())
a = list(map(int, input().split()))
cafes = set(a)
output = 0
for i in range(1, n+1):
    if a[-i] in cafes:
        cafes.remove(a[-i])
        output = a[-i]
print(output)
