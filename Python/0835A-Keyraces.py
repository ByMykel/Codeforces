#https://codeforces.com/problemset/problem/835/A

n = list(map(int, input().split()))
if n[1]*n[0] + n[3]*2 < n[2]*n[0] + n[4]*2:
    print("First")
elif n[1]*n[0] + n[3]*2 > n[2]*n[0] + n[4]*2:
    print("Second")
else:
    print("Friendship")
