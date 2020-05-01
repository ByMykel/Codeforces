#https://codeforces.com/contest/1216/problem/B

n = int(input())
a = sorted(enumerate(map(int, input().split())), key=lambda x: x[1], reverse=True)
shots = 0
output = [0] * n
for i in range(n):
    shots += a[i][1]*i + 1
    output[i] = a[i][0] + 1
print(shots)
print(*output)
