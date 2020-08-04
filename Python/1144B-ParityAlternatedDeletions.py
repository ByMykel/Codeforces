#https://codeforces.com/problemset/problem/1144/B

n = int(input())
a = sorted(list(map(int ,input().split())))
even = sum(1 for i in a if i % 2 == 0)
odd = n - even
if even == odd or even+1 == odd or even == odd+1:
    print(0)
else:
    if even > odd:
        even = even - odd - 1
        ans = 0
        for i in a:
            if even == 0:
                break
            if i % 2 == 0:
                ans += i
                even -= 1
    else:
        odd = odd - even - 1
        ans = 0
        for i in a:
            if odd == 0:
                break
            if i % 2 != 0:
                ans += i
                odd -= 1
    print(ans)
