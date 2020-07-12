#https://codeforces.com/problemset/problem/1200/A

n = int(input())
s = input()
rooms = [0] * 10
for i in s:
    if i == "L":
        for j in range(n):
            if rooms[j] == 0:
                rooms[j] = 1
                break
    elif i == "R":
        for j in range(9, -1, -1):
            if rooms[j] == 0:
                rooms[j] = 1
                break
    else:
        rooms[int(i)] = 0
print("".join(map(str, rooms)))
