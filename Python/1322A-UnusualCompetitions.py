#https://codeforces.com/contest/1322/problem/A

n = int(input())
s = input()
output = 0
count = 0
if s.count("(") != s.count(")"):
    print(-1)
else:
    for i in range(n):
        last = count
        if s[i] == "(":
            count += 1
        else:
            count += -1
        if count < 0 or last < 0:
            output += 1
    print(output)
