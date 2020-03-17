#https://codeforces.com/problemset/problem/25/A

n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(3):
    if a[i] % 2 == 0:
        count += 1
    else:
        count -= 1
even = True if count > 0 else False
for i in range(n):
    if even == True and a[i] % 2 != 0:
        print(i+1)
        break
    elif even == False and a[i] % 2 == 0:
        print(i+1)
        break
