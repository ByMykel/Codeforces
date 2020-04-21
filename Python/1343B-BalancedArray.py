#https://codeforces.com/contest/1343/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4 == 0:
        output = []
        for i in range(n//2):
            output.append(2*i + 2)
        total = sum(output)
        for i in range(n//2):
            if i == n//2 - 1:
                output.append(total)
            else:
                output.append(2*i + 1)
                total -= 2*i + 1
        print("YES")
        print(*output)
    else:
        print("NO")
