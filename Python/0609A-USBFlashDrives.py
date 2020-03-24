#https://codeforces.com/problemset/problem/609/A

n = int(input())
m = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
a = sorted(a, reverse = True)
solution = 0
for i in a:
    if m > 0:
        m -= i
        solution += 1
    else:
        break
print(solution)
