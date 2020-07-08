#https://codeforces.com/contest/1368/problem/B

n = int(input())
string = "codeforces"
a = [1] * 10
k = 1
while k < n:
    for i in range(10):
        a[i] += 1
        k = 1
        for j in a:
            k *= j
        if k >= n:
            break
output = ""
for i in range(10):
    output += string[i] * a[i]
print(output)
