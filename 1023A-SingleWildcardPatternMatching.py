#https://codeforces.com/contest/1023/problem/A

n, m = map(int, input().split())
s = input()
t = input()
 
 
if n > m + 1:
    print("NO")
else:
    if "*" in s and len(s) > 1:
        s = s.split("*")
 
        if s[0] == t[:len(s[0])] and s[1] == t[-len(s[1]):]:
            print("YES")
        elif s[1] == '' and s[0] == t[:len(s[0])]:
            print("YES")
        else:
            print("NO")
    else:
        if s == t:
            print("YES")
        elif len(s) == 1 and "*" in s:
            print("YES")
        else:
            print("NO")
