#https://codeforces.com/problemset/problem/996/A

n = int(input())
c = 0
c += int(n / 100)
c += int(n % 100 / 20)
c += int(n % 100 % 20 / 10)
c += int(n % 100 % 20 % 10 / 5)
c += int(n % 100 % 20 % 10 % 5)
print(c)
