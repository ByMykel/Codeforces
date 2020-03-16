#https://codeforces.com/contest/1077/problem/C

n = int(input())
a = [i for i in map(int, input().split())]
asort = sorted(a, reverse=True)
suma = sum(a)
solution = []
for i in range(n):
    maxnumber = asort[0]
    if a[i] == maxnumber:
        maxnumber = asort[1]
    if suma - a[i] - maxnumber == maxnumber:
        solution.append(str(i+1))
if len(solution) > 0:
    print(len(solution))
    print(" ".join(solution))
else:
    print(0)
