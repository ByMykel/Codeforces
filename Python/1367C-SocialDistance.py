#https://codeforces.com/contest/1367/problem/C

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    if n == k:
        if s.count("1") != 0:
            print(0)
        else:
            print(1)
    else:
        output = 0
        i = 0
        while i < n:
            if s[i] == "1":
                i += k
            else:
                if "1" not in s[i+1:i+k+1]:
                    output += 1
                    i += k
            i += 1
        print(output)
