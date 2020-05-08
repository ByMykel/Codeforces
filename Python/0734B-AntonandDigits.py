#https://codeforces.com/problemset/problem/734/B

k = list(map(int, input().split()))
m = min(k[0], k[2], k[3])
output = m*256 + min(k[0]-m, k[1])*32
print(output)
