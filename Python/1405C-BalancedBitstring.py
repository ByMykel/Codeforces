#https://codeforces.com/problemset/problem/1405/C

import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

t = ini()
for _ in range(t):
    n, k = inm()
    s = list(ins())
    ans = True
    count0 = count1 = 0
    for i in range(k):
        seen0 = seen1 = False
        for j in range(i, n, k):
            if s[j] == "0":
                seen0 = True
            elif s[j] == "1":
                seen1 = True
        if seen0 and seen1:
            ans = False
            break
        elif seen0:
            count0 += 1
        elif seen1:
            count1 += 1
    if count0 > k//2 or count1 > k//2:
        ans = False
    print("YES" if ans else "NO")
