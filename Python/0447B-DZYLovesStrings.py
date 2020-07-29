#https://codeforces.com/problemset/problem/447/B

s = input()
k = int(input())
w = list(map(int, input().split()))
ans = 0
for i in range(len(s)):
    ans += (i+1) * w[ord(s[i]) - 97]
for i in range(len(s), len(s)+k):
    ans += (i+1) * max(w)
print(ans)
