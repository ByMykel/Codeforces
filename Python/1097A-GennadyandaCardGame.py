#https://codeforces.com/problemset/problem/1097/A

table = input()
hand = input()
print("YES" if table[0] in hand or table[1] in hand else "NO")
