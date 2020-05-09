#https://codeforces.com/problemset/problem/1352/A

t = int(input())
for _ in range(t):
    n = input()
    output = []
    for i in range(len(n)):
        if n[i] != "0":
            output.append(n[i] + "0"*(len(n)-i-1))
    print(len(output))
    print(*output)
