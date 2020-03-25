#https://codeforces.com/problemset/problem/1196/A

q = int(input())
for i in range(q):
    candies = list(map(int, input().split()))
    print(sum(candies) // 2)
