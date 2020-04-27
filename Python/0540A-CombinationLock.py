#https://codeforces.com/problemset/problem/540/A

n = int(input())
start = input()
stop = input()
moves = 0
for i in range(n):
    if abs(int(start[i]) - int(stop[i])) > 5:
        moves += 5 - abs(int(start[i]) - int(stop[i])) % 5
    else:
        moves += abs(int(start[i]) - int(stop[i]))
print(moves)
