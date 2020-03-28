#https://codeforces.com/problemset/problem/721/A

n = int(input())
s = input()
if "B" not in s:
    print(0)
else:
    s = s.split("W")
    solution = list(filter(lambda x: x > 0, map(len, s)))
    print(len(solution))
    print(" ".join(map(str, solution)))
