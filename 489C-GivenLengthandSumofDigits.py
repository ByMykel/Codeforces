#https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
msmallest, slargest = m, s
if s/m > 9 or (m > 1 and s == 0):
    print("-1 -1")
else:
    totaln = s // 9
    s -= 9 * totaln
    msmallest -= totaln
    smallest = ""
    for i in range(msmallest):
        if i == 0 and msmallest > 1:
            smallest += "1"
            s -= 1
        elif i > 0 and i != msmallest-1:
            smallest += "0"
        else:
            smallest += str(s)
    smallest += "9" * totaln
    if "-1" in smallest:
        smallest = smallest.replace("-19", "08")
    largest = ""
    for i in range(m):
        if slargest >= 9:
            largest += str(9)
            slargest -= 9
        else:
            largest += str(slargest)
            slargest -= slargest
    print(f"{smallest} {largest}")
