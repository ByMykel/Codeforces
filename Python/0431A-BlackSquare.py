#https://codeforces.com/problemset/problem/431/A

a = list(map(int, input().split()))
s = input()
solution = 0
for i in range(1, 5):
    solution += s.count(str(i)) * a[i-1]
print(solution)
