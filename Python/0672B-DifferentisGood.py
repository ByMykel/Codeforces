#https://codeforces.com/problemset/problem/672/B

n = int(input())
s = input()
ans = n - len(set(s))
if n < 27:
    print(ans)
else:
    print(-1)
