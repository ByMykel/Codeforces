#https://codeforces.com/contest/1176/problem/A

q = int(input())
for _ in range(q):
    n = int(input())
    if n == 1:
        print(0)
    else:
        output = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
                output += 1
            elif n % 3 == 0:
                n = 2*n // 3
                output += 1
            elif n % 5 == 0:
                n = 4*n // 5
                output += 1
            else:
                output = -1
                break
        print(output)
