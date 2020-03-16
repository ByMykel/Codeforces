#https://codeforces.com/problemset/problem/1220/A

n = int(input())
s = input()
one = s.count("n")
zero = (n - one*3) // 4
solution = ["1"] * one + ["0"] * zero
print(" ".join(solution))
