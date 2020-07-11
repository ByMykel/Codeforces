#https://codeforces.com/problemset/problem/1038/A

n, k = map(int, input().split())
s = input()
characters = list(set(s))
if len(characters) < k:
    print(0)
else:
    count = [0] * len(characters)
    for i in range(len(characters)):
        count[i] = s.count(characters[i])
    count = sorted(count)
    print(count[0] * k)
