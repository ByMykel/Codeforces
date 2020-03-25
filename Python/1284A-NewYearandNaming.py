#https://codeforces.com/contest/1284/problem/A

n, m = map(int, input().split())
s = list(map(str, input().split()))
t = list(map(str, input().split()))
q = int(input())
for i in range(q):
    y = int(input()) - 1
    print(s[y % len(s)] + t[y % len(t)])
