#https://codeforces.com/problemset/problem/427/A

n = int(input())
events = tuple(map(int, input().split()))
solution, police = 0, 0
for i in range(n):
    if police == 0 and events[i] == -1:
        solution += 1
    elif police > 0 and events[i] == -1:
        police -= 1
    else:
        police += events[i]
print(solution)
