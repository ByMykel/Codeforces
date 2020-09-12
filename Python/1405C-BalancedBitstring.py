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
    for i in range(k):
        tmp = -1
        for j in range(i, n, k):
            if s[j] != "?":
                if tmp != -1 and s[j] != tmp:
                    ans = False
                    break
                tmp = s[j]
        if not ans:
            break
        else:
            if s[i] == "?":
                s[i] = tmp
    if ans:
        count0 = count1 = x = 0
        for i in range(k):
            if s[i] == "0":
                count0 += 1
            elif s[i] == "1":
                count1 += 1
            else:
                x += 1
        if x == 0 and count0 != count1:
            ans = False
        elif count0 != count1:
            if min(count0, count1) + x < max(count0, count1):
                ans = False
    print("YES" if ans else "NO")
