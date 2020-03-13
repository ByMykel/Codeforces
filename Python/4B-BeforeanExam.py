#https://codeforces.com/contest/4/problem/B

d, sumTime = map(int, input().split())
minTimel = []
maxTimel = []
 
for i in range(d):
    minTime, maxTime = map(int, input().split())
    minTimel.append(minTime)
    maxTimel.append(maxTime)
 
if d < 1 or d > 30 or sumTime < 0 or sumTime > 240 or sum(maxTimel) < sumTime or minTime > sumTime or sum(minTimel) > sumTime:
    print("NO")
else:
    print("YES")
    
    for i in range(d):
        time = min(minTimel[i] + sumTime - sum(minTimel), maxTimel[i])
        sumTime -= (time - minTimel[i]);
        print(str(time), end =" ")
