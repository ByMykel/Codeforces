#https://codeforces.com/contest/4/problem/C

def main():
    n = int(input())
    words = {}
    solution = [0] * n
    for i in range(n):
        word = input()
        if word in words:
            solution[i] = f"{word}{words[word]}"
            words[word] += 1
        else:
            solution[i] = "OK"
            words[word] = 1
    print("\n".join(solution))
main()
