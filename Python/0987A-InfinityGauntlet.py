#https://codeforces.com/problemset/problem/987/A

n = int(input())
gems = {
    "purple" : "Power", "green" : "Time", "blue" : "Space", 
    "orange" : "Soul", "red" : "Reality", "yellow" : "Mind"
}
for i in range(n):
    color = input()
    del gems[color]
print(len(gems))
for i in gems:
    print(gems[i])
