#https://codeforces.com/problemset/problem/133/A

s = input()
solution = False
for letter in s:
    if letter in "HQ9":
        solution = True
        break
print("YES" if solution else "NO")
