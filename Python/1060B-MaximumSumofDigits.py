#https://codeforces.com/contest/1060/problem/B

def suma(n):
    return sum(map(int, str(n)))
    
n = int(input())
if n <= 10:
    print(n)
else:
    first = int(str(int(str(n)[0])-1) + (len(str(n))-1)*"9")
    print(suma(first) + suma(n - first))
