#https://codeforces.com/problemset/problem/1367/A

t = int(input())
for _ in range(t):
    b = input()
    output = b[:2]
    for i in range(2, len(b)):
        if i % 2 != 0:
            output += b[i]
    print(output)
