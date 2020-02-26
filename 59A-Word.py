#https://codeforces.com/problemset/problem/59/A

s = input()
c = sum(1 for i in s if i.isupper())
print(s.upper() if c > len(s)/2 else s.lower())
