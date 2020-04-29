#https://codeforces.com/problemset/problem/1296/B

t = int(input())
for _ in range(t):
    n = int(input())
    output = 0
    while n >= 1:
        if n < 10:
            output += n
            break
        output += n - n%10
        n = n - (n - n%10) + n//10
    print(output)
