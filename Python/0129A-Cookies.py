#https://codeforces.com/problemset/problem/129/A

n = int(input())
a = list(map(int, input().split()))
suma = sum(a)
solution = 0
for i in a:
    if (suma - i) % 2 == 0:
        solution += 1
print(solution)
