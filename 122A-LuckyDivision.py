#https://codeforces.com/problemset/problem/122/A

n = int(input())
l = False
if str(n).count("4")+str(n).count("7") == len(str(n)):
    l = True
else:
    for i in range(1, n):
        lucky = str(i).count("4") + str(i).count("7") == len(str(i))
        if lucky:
            if n % i == 0:
                l = True
                break
print("YES" if l else "NO")
