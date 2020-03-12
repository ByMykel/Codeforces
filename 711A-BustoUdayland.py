#https://codeforces.com/problemset/problem/711/A

n = int(input())
solution = []
pair = False
for i in range(n):
    seats = input()
    if "OO" in seats and pair == False:
        if seats == "OO|OO":
            solution.append("++|OO")
        else:
            solution.append(seats.replace("OO", "++"))
        pair = True
    else:
        solution.append(seats)
if pair:
    print("YES")
    print("\n".join(solution))
else:
    print("NO")
