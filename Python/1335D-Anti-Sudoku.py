#https://codeforces.com/contest/1335/problem/D

t = int(input())
for _ in range(t):
    sudoku = []
    for i in range(9):
        s = input().replace("1", "2")
        sudoku.append(s)
    for i in sudoku:
        print(i)
