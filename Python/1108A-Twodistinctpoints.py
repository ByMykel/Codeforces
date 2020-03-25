#https://codeforces.com/problemset/problem/1108/A

q = int(input())
for i in range(q):
    segments = list(map(int, input().split()))
    if segments[0] != segments[3]:
        print(segments[0], segments[3])
    else:
        print(segments[0], segments[2])
