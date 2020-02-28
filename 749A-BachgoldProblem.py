#https://codeforces.com/problemset/problem/749/A

n = int(input())
solution = []
if n % 2 == 0:
    print(int(n/2))
    for i in range(0, n, 2):
        print("2 ", end="")
else:
    for i in range(0, n-1, 2):
        solution.append("2")
    solution[-1] = "3"
    print(len(solution))
    print(" ".join(solution))
