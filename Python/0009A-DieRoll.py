#https://codeforces.com/problemset/problem/9/A

best = max(map(int, input().split()))
s = {1 : "1/6", 2 : "1/3", 3 : "1/2", 4 : "2/3", 5 : "5/6", 6 : "1/1"}
print(s[7 - best])
