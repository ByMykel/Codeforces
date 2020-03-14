#https://codeforces.com/contest/189/problem/A

n, a, b, c = map(int, raw_input().split())
solution = 0
for i in xrange(n+1):
    for j in xrange(n+1):
        z = (n - a*i - b*j) / c
        if z >= 0 and z % 1 == 0:
            if n == (a*i + b*j + c*z):
                if int(i+j+z) > solution:
                    solution = int(i+j+z)
print(solution)
