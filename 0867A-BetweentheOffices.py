#https://codeforces.com/problemset/problem/867/A

n = int(input())
s = input()
print("YES" if s.count("SF") > s.count("FS") else "NO")
