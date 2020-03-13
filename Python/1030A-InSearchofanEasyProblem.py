#https://codeforces.com/problemset/problem/1030/A

n = int(input())
p = sum(map(int, input().split()))
print("HARD" if p > 0 else "EASY")
