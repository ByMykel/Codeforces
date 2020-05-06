#https://codeforces.com/problemset/problem/78/A

n = [5, 7, 5]
haiku = True
for i in range(3):
    s = input().strip()
    vowel = sum(1 for i in s if i in "aeiou")
    if vowel != n[i]:
        haiku = False
        break
print("YES" if haiku else "NO")
