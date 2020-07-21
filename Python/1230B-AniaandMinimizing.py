#https://codeforces.com/problemset/problem/1230/B

n, k = map(int, input().split())
s = input()
if k == 0:
    print(s)
elif n == 1:
    print(0)
else:
    s = list(s)
    i = 1
    if s[0] != "1":
        s[0] = "1"
        k -= 1
    while k:
        if s[i] != "0":
            s[i] = "0"
            k -= 1
        i += 1
        if i == n:
            break
    print("".join(s))
