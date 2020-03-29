#https://codeforces.com/contest/1143/problem/A

n = int(input())
doors = list(map(int, input().split()))[::-1]
left = n - doors.index(0)
right = n - doors.index(1)
print(min(left, right))
