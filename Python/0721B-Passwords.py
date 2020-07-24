#https://codeforces.com/problemset/problem/721/B

n, k = map(int, input().split())
pw = []
for _ in range(n):
    pw.append(input())
s = input()
pw = sorted(pw, key=len)
ans1 = 1
ans2 = 0
for i in pw:
    if len(s) < len(i):
        break
    if len(s) == len(i):
        ans2 += 1
    if len(s) > len(i):
        ans1 += 1
ans2 += ans1 + ((ans1+ans2-2)//k) * 5 - 1
ans1 += ((ans1-1)//k) * 5
print(ans1, ans2)
