#https://codeforces.com/problemset/problem/734/A

n = int(input())
games = input()
gamesA = len(games.replace("D", ""))
gamesD = n - gamesA
if gamesA > gamesD:
    print("Anton")
elif gamesA < gamesD:
    print("Danik")
else:
    print("Friendship")
