#https://codeforces.com/problemset/problem/1266/B

t = int(input())
a = list(map(int, input().split()))
for n in a:
    if n < 15:
        print("NO")
        continue
    m = n % 14
    if m > 0 and m <= 6:
        print("YES")
    else:
        print("NO")
