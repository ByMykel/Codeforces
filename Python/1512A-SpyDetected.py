#https://codeforces.com/problemset/problem/1512/A

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))
 
t = ini()
for i in range(t):
    n = ini()
    a = inl()
    count = [0] * 101
    index = [-1] * 101
    for i in range(n):
        count[a[i]] += 1
        index[a[i]] = i 
    print(index[count.index(1)] + 1)
