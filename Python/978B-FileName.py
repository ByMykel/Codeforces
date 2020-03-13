#https://codeforces.com/contest/978/problem/B

n = int(input())
s = input()
countx = 0
solution = 0
for i in s:
    if i == "x":
        countx += 1
        if countx >= 3:
            solution += 1
    else:
        countx = 0
print(solution)
