#https://codeforces.com/contest/1350/problem/A

def ff(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    while k:
        f = ff(n)
        if f == 2:
            n += 2 * k
            break
        else:
            n += f
        k -= 1
    print(n)
