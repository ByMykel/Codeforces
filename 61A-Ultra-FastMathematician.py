#https://codeforces.com/problemset/problem/61/A

a = input()
b = input()
solution = []
for i in range(len(a)):
    if bool(int(a[i])) ^ bool(int(b[i])):
        solution.append(str(1))
    else:
        solution.append(str(0))
print("".join(solution))
