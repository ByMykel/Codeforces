#https://codeforces.com/contest/158/problem/B

n = int(input())
children = list(map(int, input().split()))
ntaxis = 0
s1 = children.count(1)
s2 = children.count(2)
s3 = children.count(3)
s4 = children.count(4)

if s1 == s3:
    ntaxis += s1
    s1 = 0
    s3 = 0
elif s1 > s3:
    ntaxis += s3
    s1 -= s3
    s3 = 0
else:
    ntaxis += s1
    ntaxis += s3 - s1
    s1 = 0

if s2 % 2 == 0:
    ntaxis += s2 / 2
    s2 = 0
else:
    ntaxis += s2 // 2
    s2 = 1

if s1 > 0 and s2 > 0:
    ntaxis += 1
    s2 -= 1
    if s1 - 2 >= 0:
        s1 -= 2
        if s1 >= 4:
            ntaxis += s1 // 4
            s1 -= (s1 // 4)*4
            if s1 > 0:
                ntaxis += 1 
        elif s1 > 0:
            ntaxis += 1
    else:
        s1 -= 1
elif s1 == 0 and s2 > 0:
    ntaxis += 1
    s2 -= 1
elif s1 > 0 and s2 == 0:
    if s1 >= 4:
        ntaxis += s1 // 4
        s1 -= (s1 // 4)*4
        if s1 > 0:
            ntaxis += 1
    else:
        ntaxis += 1 

print(int(ntaxis + s4))
