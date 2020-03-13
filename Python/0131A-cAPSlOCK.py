#https://codeforces.com/problemset/problem/131/A

word = input()
if len(word) == 1:
    if word.isupper():
        print(word.lower())
    else:
        print(word.upper())
elif word.isupper():
    print(word.lower())
elif word[1:].isupper():
    print(word.capitalize())
else:
    print(word)
