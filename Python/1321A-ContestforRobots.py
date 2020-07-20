#https://codeforces.com/problemset/problem/1321/A

import math
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a == b:
    print(-1)
else:
    counta = 0
    countb = 0
    for i in range(n):
        if a[i] == 1 and b[i] == 0:
            counta += 1
        elif a[i] == 0 and b[i] == 1:
            countb += 1
    if counta == 0:
        print(-1)
    else:
        print(countb//counta + 1)
        
