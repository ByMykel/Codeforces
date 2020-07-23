#https://codeforces.com/contest/1073/problem/B

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = [0] * n
checked = set()
j = 0
for i in range(n):
    if b[i] in checked:
        continue
    else:
        count = 0
        while b[i] != a[j]:
            checked.add(a[j])
            count += 1
            j += 1
        ans[i] = count + 1
        checked.add(b[i])
        j += 1
print(*ans)
