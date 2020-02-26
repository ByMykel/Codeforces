#https://codeforces.com/problemset/problem/110/A

n = int(input())
c = sum(1 for i in str(n) if i in ["4", "7"])
print("YES" if str(c) in ["4", "7"] else "NO")
