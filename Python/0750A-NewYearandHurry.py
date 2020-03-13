#https://codeforces.com/problemset/problem/750/A

n, k = map(int, input().split())
k = 240 - k
solution = 0
for i in range(1, n+1):
    if k - i*5 >= 0:
        k -= i*5
        solution +=1
    else:
        break
print(solution)
