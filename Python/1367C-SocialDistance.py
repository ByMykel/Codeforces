#https://codeforces.com/contest/1367/problem/C

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    s = ("0"*k + s + "0"*k).split("1")
    output = 0
    for i in s:
        output += (len(i)-k) // (k+1)
    print(output)
