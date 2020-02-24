n = int(input())
words = {}
solution = []
for i in range(n):
    word = input()
    if word in words:
        solution.append(f"{word}{words[word]}")
        words[word] += 1
    else:
        solution.append("OK")
        words[word] = 1
for i in solution:
    print(i)
