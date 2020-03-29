#https://codeforces.com/problemset/problem/658/A

n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
pointsl, pointsr = 0, 0
timel, timer = 0, 0
for i in range(n):
    timel += t[i]
    timer += t[-i-1]
    pointsl += max(0, p[i] - c*timel)
    pointsr += max(0, p[-i-1] - c*timer)
if pointsl > pointsr:
    print("Limak")
elif pointsl < pointsr:
    print("Radewoosh")
else:
    print("Tie")
