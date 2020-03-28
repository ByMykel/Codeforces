#https://codeforces.com/problemset/problem/721/A

n = int(input())
s = input()
if "B" not in s:
    print(0)
else:
    s = s.split("W")
    solution = list(map(len, filter(lambda x: len(x) > 0, s)))
    print(len(solution))
    print(" ".join(map(str, solution)))
