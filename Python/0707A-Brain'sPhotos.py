#https://codeforces.com/problemset/problem/707/A

n, m = map(int, input().split())
color = False
for i in range(n):
    pixels = input()
    if "C" in pixels or "M" in pixels or "Y" in pixels:
        color = True
        break
print("#Color" if color else "#Black&White")
