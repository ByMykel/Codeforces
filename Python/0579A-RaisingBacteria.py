#https://codeforces.com/problemset/problem/579/A

import math
n = int(input())
if n == 1:
    print(1)
else:
    start = int(math.log2(n))
    solution = 0
    for i in range(start, -1, -1):
        bacteria  = 2**i
        if n == 0:
            break
        elif bacteria  <= n:
            n -= bacteria 
            solution += 1
    print(solution)
  
"""
One line solution:
print(str(bin(int(input()))).count("1"))
"""
