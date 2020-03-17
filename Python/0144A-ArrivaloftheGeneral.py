#https://codeforces.com/problemset/problem/144/A

n = int(input())
a = list(map(int, input().split()))
minimo = n - a[::-1].index(min(a)) - 1
maximo = a.index(max(a))
if minimo < maximo:
    print(maximo + (n - minimo - 1) - 1)
else:
    print(maximo + (n - minimo - 1))
