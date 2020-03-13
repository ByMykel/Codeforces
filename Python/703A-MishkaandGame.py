#https://codeforces.com/contest/703/problem/A

n = int(input())
mwins, cwins = 0, 0
for i in range(n):
    m, c = map(int, input().split())
    if m > c:
        mwins += 1
    elif m < c:
        cwins += 1
if mwins == cwins:
    print("Friendship is magic!^^")
else:
    print("Mishka" if mwins > cwins else "Chris")