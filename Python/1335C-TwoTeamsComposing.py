#https://codeforces.com/problemset/problem/1335/C

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    different = len(set(a))
    most = Counter(a).most_common(1)[0][1]
    print(max(min(different-1, most), min(different, most-1)))
