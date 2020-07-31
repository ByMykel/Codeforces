#https://codeforces.com/problemset/problem/801/B

import string
x = input()
y = input()
alpha = string.ascii_lowercase
ans = ""
for i in range(len(x)):
    if alpha.index(x[i]) == alpha.index(y[i]):
        ans += x[i]
    elif alpha.index(x[i]) > alpha.index(y[i]):
        ans += y[i]
    else:
        ans = -1
        break
print(ans)
