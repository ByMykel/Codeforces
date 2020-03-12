#https://codeforces.com/problemset/problem/82/A

n = int(input()) - 1
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
while n >= 5:
    n -= 5
    n = n // 2
print(names[n])
