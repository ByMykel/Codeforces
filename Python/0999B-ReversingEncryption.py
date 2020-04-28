#https://codeforces.com/problemset/problem/999/B

n = int(input())
s = input()
for i in range(1, n):
    if n % i == 0:
        s = s[:i][::-1] + s[i:]
print(s[::-1])
