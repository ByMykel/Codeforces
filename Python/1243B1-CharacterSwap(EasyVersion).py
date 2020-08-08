#https://codeforces.com/problemset/problem/1243/B1

k = int(input())
for i in range(k):
    n = int(input())
    s = input()
    t = input()
    ans = True
    count = 2
    index = []
    if s == t:
        print("YES")
        break
    for i in range(n):
        if s[i] != t[i]:
            count -= 1
            if count < 0:
                ans = False
                break
            index.append(i)
    if ans == True:
        ans = False
        for i in range(len(index)):
            first = index[i]
            if ans:
                break
            for j in range(len(index)):
                second = index[j]
                if s[:first] + t[second] + s[first+1:] == t[:second] + s[first] + t[second+1:]:
                    ans = True
                    break
    print("Yes" if ans else "No")
