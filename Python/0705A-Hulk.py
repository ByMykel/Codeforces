#https://codeforces.com/problemset/problem/705/A

n = int(input())
o = ["I hate", "I love"]
solution = [o[i % 2] for i in range(n)]
print(" that ".join(solution), "it")
