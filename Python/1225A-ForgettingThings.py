#https://codeforces.com/problemset/problem/1225/A

a, b = map(int, input().split())
if a == b:
    print(a*10, b*10+1)
else: 
    if b*10 == a+1:
        print(a, b*10)
    elif a > b or a+1 != b:
        print(-1)
    else:
        print(a, b)
