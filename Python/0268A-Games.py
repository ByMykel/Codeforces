#https://codeforces.com/problemset/problem/268/A

n = int(input())
h = []
a = []
solution = 0
for i in range(n):
    numbers = list(map(int, input().split()))
    h.append(numbers[0])
    a.append(numbers[1])
for i in range(n):
    if h[i] in a:
        solution += a.count(h[i])
print(solution)
